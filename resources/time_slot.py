
from flask_restful import Resource, reqparse
from models.time_slot import TimeSlotModel
from models.calendar import CalendarModel




class TimeSlot(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('calendar_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('time_started',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('duration',
                        type=int,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('description',
                        type=str,
                        required=False,
                        help="Description is optional"
                        )
    # CLASS methods
    def __init__(self):
        self.last_selected_slot_id = 0  # ostatnio wybrany obiekt


    # REQUESTS

    def post(self):
        data = TimeSlot.parser.parse_args()
        if CalendarModel.find_by_id(data['calendar_id']):
            try:
                slot_available = self.check_time_slot_available(data['time_started'], data['duration'], data['calendar_id'])
            except:
                return {'message': 'wrong data parsing'}
            if slot_available:
                time_slot = TimeSlotModel(**data)
                time_slot.save_to_db()
                return{'message': 'time slot saved'}
            return{'message': 'slot already booked'}
        return {'message': 'calendar with id: {} not found'.format(data['calendar_id'])}

    def put(self,):
        # put last selected time slot
        time_slot = TimeSlotModel.find_by_id(self.last_selected_slot_id)
        if time_slot:
            data = TimeSlot.parser.parse_args()
            if self.check_time_slot_available(data['time_started'], data['duration']):
                time_slot.time_started = data['time_started']
                time_slot.duration = data['duration']
                time_slot.duration = data['description']
                time_slot.save_to_db()
                return {'message': 'time slot updated'}
            return {'message': 'new time slot not available'}
        return {'message': 'time slot not found'}


    def get(self):
        data = TimeSlot.parser.parse_args()
        #ToDo jak nie ma?
        TimeSlotModel.get_slot_id(data['client_id'], data['time_started'])
        self.last_selected_slot_id = TimeSlotModel.id
        return {'time_slot_id': self.last_selected_slot_id}

    # OTHER METHODS

    def check_time_slot_available(self, start, duration, calendar_id):
        for time_slot in TimeSlotModel.query.all():
            if time_slot.check_conflict(start, duration, calendar_id):
                return False
        return True



class TimeSlotsList(Resource):

    # REQUESTS

    def get(self, calendar_id):
        time_slots_list = []
        for time_slot in TimeSlotModel.query.all():
            if time_slot.calendar_id == calendar_id:
                time_slots_list.append(time_slot.json())
        return {'time_slots': time_slots_list}

