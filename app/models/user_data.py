from app import db
from dataclasses import dataclass

@dataclass
class UserData(db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(120), nullable=False)
    lastname: str = db.Column(db.String(120), nullable=False)
    phone: str = db.Column(db.String(120), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates='data')

