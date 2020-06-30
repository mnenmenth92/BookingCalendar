from db import db
from models.user import UserModel


# Admin can delete users
class AdminModel(UserModel):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }



    def json(self):
        return {'username:': self.username}
