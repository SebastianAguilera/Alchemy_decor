from dataclasses import dataclass
from app import db
from typing import List

@dataclass
class Role(db.Model):
    __tablename__ = 'roles'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False, unique=True)
    description: str = db.Column(db.String(255), nullable=True)
    
    # Relación con User
    users: List['User'] = db.relationship('User', back_populates='role')

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(120), nullable=False, unique=True)
    email: str = db.Column(db.String(255), nullable=False, unique=True)
    password: str = db.Column(db.String(255), nullable=False)

    # Foreign key for role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship("Role", back_populates="users")

@dataclass
class UserData(db.Model):
    __tablename__ = 'user_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name: str = db.Column(db.String(120), nullable=False)
    last_name: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(255), nullable=True)
    phone_number: str = db.Column(db.String(15), nullable=True)

    # Foreign key for user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="user_data")
