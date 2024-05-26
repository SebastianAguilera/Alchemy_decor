from dataclasses import dataclass


@dataclass(init=False, repr=True, eq=True)
class UserData:
    surname: str
    phone: str
    address: str
    city: str
    country: str


"""
from app import db

@dataclass
class UserData(db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(120), nullable=True)
    lastname: str = db.Column(db.String(120), nullable=True)
    phone: str = db.Column(db.String(120), nullable=True)

    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates='data')
"""

