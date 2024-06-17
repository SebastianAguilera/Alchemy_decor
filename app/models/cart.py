from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Cart(db.Model):
    __tablename__ = 'carts'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart: str = db.Column(db.String(120), nullable=False)
    state: str = db.Column(db.String(120), nullable=False)
    deprice: str = db.Column(db.String(120), nullable=False)

    def save(self) -> 'Cart':
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls) -> List['Cart']:
        return cls.query.all()

    @classmethod
    def find(cls, id: int) -> 'Cart':
        return cls.query.get(id)

    @classmethod
    def find_by(cls, **kwargs) -> List['Cart']:
        return cls.query.filter_by(**kwargs).all()
