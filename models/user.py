from db import db


# UserModel is most basic user model.
# User model stores username and password.
# it has methods for database read, write and find by name used also by children classes
# children classes: Client, Admin
class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    user_type = db.Column(db.String(80))

    # clients and admins inherit the same data base
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username:': self.username}

    # find user by name in database
    @classmethod
    def find_by_name(cls, username):
        return cls.query.filter_by(username=username).first()

    # save class to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete class from database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()