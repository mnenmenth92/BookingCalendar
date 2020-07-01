
from flask_restful import Resource, reqparse
from models.admin import AdminModel
from resources.user import User


class Admin(User):

    def post(self):
        data = User.parser.parse_args()
        if AdminModel.find_by_name(data['username']):
            return{'message': "Admin already exists"}, 400

        admin = AdminModel(data['username'], data['password'])

        try:
            admin.save_to_db()
        except:
            return {'message': 'An error occured during item insertion'}, 500  # Internal server error

        return admin.json(), 201




class AdminList(Resource):
    def get(self):
        return {'admins': [admin.json() for admin in AdminModel.query.all()]}
