from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Category(db.Model):
    __tablename__ = 'categories'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    products = db.relationship("Product", back_populates='category')

"""
    #BORRAR

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
    
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
    """
