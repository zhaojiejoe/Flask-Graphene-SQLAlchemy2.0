# coding = utf-8
from app import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))

    addresses = db.relationship('AddressModel', backref='user')

    __tablename__ = 'user'

    def save(self):
        db.session.add(self)
        db.session.commit()


class AddressModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    __tablename__ = 'address'
