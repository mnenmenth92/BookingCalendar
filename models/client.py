from db import db
from models.user import UserModel


# client owns calendars
class ClientModel(UserModel):
    __tablename__ = 'client'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    calendars = db.relationship('CalendarModel', lazy='dynamic')
    # inherited from user
    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }

    # returns json with username and list of calendars
    def json(self):
        return {'username:': self.username, 'calendars': [calendars.json() for calendars in self.calendars.all()]}
