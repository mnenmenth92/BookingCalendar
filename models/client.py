from db import db

class ClientModel(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    calendars = db.relationship('CalendarModel', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username:': self.username, 'calendars': [calendars.json() for calendars in self.calendars.all()]}


    @classmethod
    def find_by_name(cls, username):
        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()