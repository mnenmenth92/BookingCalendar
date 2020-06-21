from flask import Flask
from flask_restful import Api
from db import db
from resources.calendar import Calendar, CalendarList
from resources.time_slot import TimeSlot, TimeSlotsList
from resources.client import Client, ClientList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Calendar, '/calendar/<string:name>')
api.add_resource(CalendarList, '/calendars')
api.add_resource(Client, '/client/<string:name>')
api.add_resource(ClientList, '/client')
api.add_resource(TimeSlot, '/time_slot')
api.add_resource(TimeSlotsList, '/time_slots_list/<int:calendar_id>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)