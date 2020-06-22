
from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    # REQUESTS

    def post(self):
        data = User.parser.parse_args()

        if UserModel.find_by_name(data['username']):
            return{'message': "User already exists"}, 400

        user = UserModel(data['username'], data['password'])

        try:
            user.save_to_db()
        except:
            return {'message': 'An error occured during item insertion'}, 500  # Internal server error

        return user.json(), 201



    def delete(self, name):
        user = UserModel.find_by_name(name)
        if user:
            user.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'No such item'}



class UserList(Resource):
    def get(self):
        return {'users': [calendar.json() for calendar in CalendarModel.query.all()]}
