from dataclasses import dataclass
from app import db

@dataclass
class UserData(db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(120), nullable=True)
    lastname: str = db.Column(db.String(120), nullable=True)
    phone: str = db.Column(db.String(120), nullable=True)
    address: str = db.Column(db.String(120), nullable=False)
    city: str   = db.Column(db.String(120), nullable=False)
    country: str = db.Column(db.String(120), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates='data')

    def __init__(self, firstname: str = None, lastname: str = None, phone: str = None, address: str = None, city: str = None, country: str = None):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country



