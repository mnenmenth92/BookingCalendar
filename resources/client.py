
from flask_restful import Resource, reqparse
from models.client import ClientModel


class Client(Resource):

    # REQUESTS



    def post(self):
        # ToDo zebrac dane na poczatku, zobaczyc jak ogarnac parser z usera.
        if ClientModel.find_by_name(name):
            return {'message': "The client with name'{}'already exists".format(name)}, 400

        client = ClientModel(name)
        try:
            client.save_to_db()
        except:
            return {'message': 'An error occured during item insertion'}, 500  # Internal server error

        return client.json(), 201

    def delete(self, name):
        client = ClientModel.find_by_name(name)
        if client:
            client.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'No such item'}


class ClientList(Resource):
    def get(self):
        return {'client': [client.json() for client in ClientModel.query.all()]}
