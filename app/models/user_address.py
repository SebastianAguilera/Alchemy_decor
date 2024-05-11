from app import db
from dataclasses import dataclass

@dataclass
class UserAddress(db.Model):
    __tablename__ = 'users_address'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    province: str = db.Column(db.String(120), nullable=False)
    postal_code: str = db.Column(db.String(120), nullable=False)
    street: str = db.Column(db.String(120), nullable=False)
    number: int = db.Column(db.Integer, nullable=False)
    floor: str = db.Column(db.String(120), nullable=True)
    apartment: str = db.Column(db.String(120), nullable=True)
    user_data_id = db.Column('user_data_id', db.Integer, db.ForeignKey('users_data.id'))
    user_data = db.relationship("UserData", back_populates='user_addresses')


