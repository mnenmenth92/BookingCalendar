
from flask_restful import Resource, reqparse
from models.calendar import CalendarModel


class Calendar(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('client_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id."
                        )

    # post calendar to database
    def post(self, name):
        # if requested calendar do n ot already exist
        # save it to database
        if CalendarModel.find_by_name(name):
            return{'message': "The calendar with name'{}'already exists".format(name)}, 400

        data = Calendar.parser.parse_args()
        calendar = CalendarModel(name, data['client_id'])
        try:
            calendar.save_to_db()
        except:
            return {'message': 'An error occured during item insertion'}, 500  # Internal server error

        return calendar.json(), 201

    # delete calendar from database
    def delete(self, name):
        calendar = CalendarModel.find_by_name(name)
        if calendar:
            calendar.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'No such item'}


class CalendarList(Resource):
    # returns calendar list json
    def get(self):
        return {'calendars': [calendar.json() for calendar in CalendarModel.query.all()]}
