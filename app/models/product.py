from dataclasses import dataclass
from .category import Category
from typing import List
from app import db

@dataclass
class Product(db.Model):
    __tablename__ = 'products'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    stock: int = db.Column(db.Integer, nullable=False)
    #relacion con producto
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates='products')
    """
    #relacion con color
    colors = db.relationship("Color", secondary="category_color", back_populates="categorys")
    colors = db.relationship("Color", secondary="category_color", back_populates="categorys")
    
    colors = db.relationship("Color", secondary="category_color", back_populates="categorys")  
    
    #relacion con carrito
    carts = db.relationship("Cart", secondary="cart_category", back_populates="categorys")
    """

    def __init__(self, category: Category = None):
        self.data = category

    def save(self) -> 'Product':
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls) -> List['Product']:
        return cls.query.all()

    @classmethod
    def find(cls, id: int) -> 'Product':
        return cls.query.get(id)

    @classmethod
    def find_by(cls, **kwargs) -> List['Product']:
        return cls.query.filter_by(**kwargs).all()
    


    """
    def add_category(self, category):
        if category not in self.categorys:
            self.categorys.append(category)
    
    def remove_category(self, category):
        if category in self.categorys:
            self.categorys.remove(category)    

    """
