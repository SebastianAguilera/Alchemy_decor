from dataclasses import dataclass, field
from .user_data import UserData
from typing import List
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(120), unique=True, nullable=False)
    email: str = db.Column(db.String(120), nullable=False)
    __password: str = db.Column('password', db.String(255), nullable=False)
    password: str = field(init=False)
    data = db.relationship('UserData', back_populates='user', uselist=False)

    def __init__(self, user_data: UserData = None):
        self.data = user_data

    def __post_init__(self):
        self.password = self.__password

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
    
    """
    Encriptar password para cumplir con la tarea de seguridad #16
    """
    #TODO: Refactorizar el código para que sea más legible y mantenible utilizando los principios SOLID.
    @property
    def password(self):
        raise AttributeError('password: campo de lectura no permitida')

    @password.setter
    def password(self, password):
        self.__password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.__password, password)

 

