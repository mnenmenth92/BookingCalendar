
from flask_restful import Resource, reqparse
from models.client import ClientModel


class Client(Resource):

    # REQUESTS

    def post(self, name):
        if ClientModel.find_by_name(name):
            return {'message': "The client with name'{}'already exists".format(name)}, 400

        data = client.parser.parse_args()
        client = ClientModel(name, data['client_id'])
        try:
            client.save_to_db()
        except:
            return {'message': 'An error occured during item insertion'}, 500  # Internal server error

        return client.json(), 201

    def delete(self, name):
        if ClientModel.find_by_name(name):
            client.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'No such item'}


class ClientList(Resource):
    def get(self):
        return {'client': [client.json() for client in ClientModel.query.all()]}
