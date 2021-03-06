from db import db
from datetime import datetime, timedelta

from config import time_format

# TimeSlot is basic unit that can be booked
# it can be assigned to calendar (knowing its id)
class TimeSlotModel(db.Model):
    __tablename__ = 'time_slot'

    id = db.Column(db.Integer, primary_key=True)
    time_started = db.Column(db.String(20))
    duration = db.Column(db.Integer)
    description = db.Column(db.String(500))

    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    calendar = db.relationship('CalendarModel')

    def __init__(self, calendar_id, time_started, duration, description=''):

        self.calendar_id = calendar_id
        self.time_started = time_started
        self.duration = duration  # minutes
        self.description = description

    # check if input is in conflict with time slot
    def check_conflict(self, start, duration, calendar_id):
        time_started = self.string_to_time(start)
        time_ended = time_started + timedelta(minutes=duration)
        # cenflict boolean sentence:
        # if time is between start and stop of time slot
        # or its start is less and end is greater
        time_clonflicted = (self.check_if_time_between(time_started) or self.check_if_time_between(time_ended)
                            or self.get_start_time() > time_started and self.get_end_time() < time_ended)
        return calendar_id == self.calendar_id and time_clonflicted

    # string formated time to datetime
    def string_to_time(self, string_time):
        return datetime.strptime(string_time, time_format)

    # datetime from start string
    def get_start_time(self):
        return self.string_to_time(self.time_started)

    # datetime from end string
    def get_end_time(self):
        time = self.string_to_time(self.time_started) + timedelta(minutes=self.duration)
        return time

    # checks if input time is between start and end of timeslot
    def check_if_time_between(self, _time):
        return _time >= self.get_start_time() and _time <= self.get_end_time()

    def update(self, time_started, duration):
        self.time_started = time_started
        self.duration = duration

    # returns json with id of owning calendar, time started, duration and description
    def json(self):
        return {'calendar_id': self.calendar_id,
                'time_started': self.time_started,
                'duration': self.duration,
                'description': self.description
                }

    # returns time slots id
    @classmethod
    def get_slot_id(cls, calendar_id, start_time):
        selected_time_slot =  cls.query.filter_by(calendar_id=calendar_id, time_started=start_time).first()
        return selected_time_slot.id

    # finds slot by id
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # save class to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete class from database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
