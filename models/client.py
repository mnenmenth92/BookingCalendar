from db import db
from models.user import UserModel

class ClientModel(UserModel):
    __tablename__ = 'client'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    calendars = db.relationship('CalendarModel', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }



    def json(self):
        return {'username:': super.username, 'calendars': [calendars.json() for calendars in self.calendars.all()]}
