from db import db

# CalendarModel has to be assigned to Client
# it alse contains time slots
class CalendarModel(db.Model):
    __tablename__ = 'calendar'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    time_slots = db.relationship('TimeSlotModel', lazy='dynamic')

    clients_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('ClientModel')

    def __init__(self, name, clients_id):
        self.name = name
        self.clients_id = clients_id
    # returns calendars name, id and contained time slots list
    def json(self):
        return {'name:': self.name, 'calendar id': self.id, 'time_slots': [time_slot.json() for time_slot in self.time_slots.all()]}

    # find calendar in database by name
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    # find calendar in database by id
    # needed for assigning time slots to calendars (it is done by calendars id)
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    # save class to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete class from database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
