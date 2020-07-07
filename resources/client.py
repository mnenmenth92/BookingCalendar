
from flask_restful import Resource, reqparse
from models.client import ClientModel
from resources.user import User


class Client(User):

    # post client - save it to database
    def post(self):
        data = User.parser.parse_args()
        if ClientModel.find_by_name(data['username']):
            return{'message': "Client already exists"}, 400

        client = ClientModel(data['username'], data['password'])

        try:
            client.save_to_db()
        except:
            return {'message': 'An error occured during item insertion'}, 500  # Internal server error

        return client.json(), 201




class ClientList(Resource):
    # returns list of clients json
    def get(self):
        return {'client': [client.json() for client in ClientModel.query.all()]}
