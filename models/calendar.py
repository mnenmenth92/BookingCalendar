from db import db

class CalendarModel(db.Model):
    __tablename__ = 'calendar'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    time_slots = db.relationship('TimeSlotModel', lazy='dynamic')

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('ClientModel')

    def __init__(self, name, client_id):
        self.name = name
        self.client_it = client_id


    def json(self):
        return {'name:': self.name, 'time_slots': [time_slot.json() for time_slot in self.time_slots.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

