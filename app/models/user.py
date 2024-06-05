from dataclasses import dataclass
from .user_data import UserData
from typing import List
from app import db

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(120), unique=True, nullable=False)
    email: str = db.Column(db.String(120), nullable=False)
    password: str = db.Column(db.String(120), unique=True, nullable=False)
    data = db.relationship('UserData', back_populates='user', uselist=False)

    def __init__(self, user_data: UserData = None):
        self.data = user_data

    def save(self) -> 'User':
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def all(cls) -> List['User']:
        return cls.query.all()
    
    @classmethod
    def find(cls, id: int) -> 'User':
        return cls.query.get(id)
    
    @classmethod
    def find_by(cls, **kwargs) -> List['User']:
        return cls.query.filter_by(**kwargs).all()
    
        

