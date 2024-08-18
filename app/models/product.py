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
    #relacion con category
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates='products')
    #relacion con color
    color_products = db.relationship("ProductColor", back_populates="product") 
    #relacion con order
    order_products = db.relationship("OrderProduct", back_populates="product", cascade="all, delete-orphan")
    
    def __init__(self, category: Category = None):
        self.data = category
