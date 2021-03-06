from flask import Flask
from flask_restful import Api
from db import db
from resources.calendar import Calendar, CalendarList
from resources.time_slot import TimeSlot, TimeSlotsList
from resources.client import Client, ClientList
from resources.user import User, UserList
from resources.admin import Admin, AdminList

# set flask webserver
app = Flask(__name__)
# set database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

# create database
@app.before_first_request
def create_tables():
    db.create_all()

# resources:
api.add_resource(Calendar, '/calendar/<string:name>')
api.add_resource(CalendarList, '/calendars')
api.add_resource(Client, '/client')
api.add_resource(ClientList, '/clients')
api.add_resource(User, '/user')
api.add_resource(UserList, '/users')
api.add_resource(TimeSlot, '/time_slot', '/time_slot/<int:time_slot_id>')
api.add_resource(TimeSlotsList, '/time_slots_list/<int:calendar_id>')
api.add_resource(Admin, '/admin')
api.add_resource(AdminList, '/admins')


if __name__ == '__main__':
    # run webserver
    db.init_app(app)
    app.run(port=5000, debug=True)