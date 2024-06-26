from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Color(db.Model):
    __tablename__ = 'colors'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    products = db.relationship("ProductColor", back_populates="color")

    def save(self) -> 'Color':
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls) -> List['Color']:
        return cls.query.all()

    @classmethod
    def find(cls, id: int) -> 'Color':
        return cls.query.get(id)

    @classmethod
    def find_by(cls, **kwargs) -> List['Color']:
        return cls.query.filter_by(**kwargs).all()
