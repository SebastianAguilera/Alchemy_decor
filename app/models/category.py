from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Category(db.Model):
    __tablename__ = 'categories'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    #products = db.relationship("Product", back_populates='category')

    def save(self) -> 'Category':
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def all(cls) -> List['Category']:
        return cls.query.all()

    @classmethod
    def find(cls, id: int) -> 'Category':
        return cls.query.get(id)

    @classmethod
    def find_by(cls, **kwargs) -> List['Category']:
        return cls.query.filter_by(**kwargs).all()

    """
    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
    
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
    """
