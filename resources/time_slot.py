
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


    # REQUESTS

    def post(self):
        data = TimeSlot.parser.parse_args()
        if CalendarModel.find_by_id(data['calendar_id']):
            try:
                slot_available = self.check_time_slot_available(data['time_started'], data['duration'], data['calendar_id'])
            except Exception as e:
                print(e)
                return {'message': 'wrong data parsing'}
            if slot_available:
                time_slot = TimeSlotModel(**data)
                time_slot.save_to_db()
                return{'message': 'time slot saved'}
            return{'message': 'slot already booked'}
        return {'message': 'calendar with id: {} not found'.format(data['calendar_id'])}

    def put(self, time_slot_id):
        # put last selected time slot
        time_slot = TimeSlotModel.find_by_id(time_slot_id)
        if time_slot:                                           # if current time slot found
            data = TimeSlot.parser.parse_args()                 # get data
            if CalendarModel.find_by_id(data['calendar_id']):   # than if selected calendar exist
                try:
                    slot_available = self.check_time_slot_available(data['time_started'], data['duration'], data['calendar_id'], time_slot_id)
                except Exception as e:
                    print(e)
                    return {'message': 'wrong data parsing'}
                if slot_available:                              # and slot is available update time slot
                    # ToDo - poprawić do jednej linijki
                    time_slot.time_started = data['calendar_id']
                    time_slot.time_started = data['time_started']
                    time_slot.duration = data['duration']
                    time_slot.duration = data['description']
                    time_slot.save_to_db()
                    return {'message': 'time slot updated'}
                return {'message': 'new time slot not available'}
            return {'message': 'time slot not found'}
        return {'message': 'calendar with id: {} not found'.format(data['calendar_id'])}

    def get(self):
        data = TimeSlot.parser.parse_args()
        selected_slot_id = TimeSlotModel.get_slot_id(data['calendar_id'], data['time_started'])
        return {'time_slot_id': selected_slot_id}

    # OTHER METHODS

    def check_time_slot_available(self, start, duration, calendar_id, slot_id=-1):
        # slot_id nie potrzebny przy post, potrzebny przy put
        for time_slot in TimeSlotModel.query.all():
            if time_slot.get_slot_id(time_slot.calendar_id, time_slot.time_started) != slot_id:
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

