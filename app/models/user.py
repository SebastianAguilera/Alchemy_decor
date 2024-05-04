from app import db
from dataclasses import dataclass
from .user_data import UserData

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(120), unique=True, nullable=False)
    email: str = db.Column(db.String(120), nullable=False)
    password: str = db.Column(db.String(120), unique=True, nullable=False)
    userdata = db.relationship('UserData', back_populates='user', uselist=False)

    def __init__(self, user_data: UserData = None):
        self.data = user_data

