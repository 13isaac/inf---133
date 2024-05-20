import json
from database import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    roles=db.Column(db.String(50), nullable=False)
    password_hash=db.Column(db.String(128), nullable=False)

    def __init__(self,username,roles,password):
        self.username=username
        self.roles=json.dumps(roles)
        self.password_hash=generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()