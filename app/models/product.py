from dataclasses import dataclass
from app import db

@dataclass
class Product(db.Model):
    __tablename__ = 'products'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    stock: int = db.Column(db.Integer, nullable=False)
  

"""
    #relacion con color
    colors = db.relationship("Color", secondary="product_color", back_populates="products")
    #relacion con categoria
    category = db.relationship("Category", back_populates='product')
    #relacion con carrito
    carts = db.relationship("Cart", secondary="cart_product", back_populates="products")
"""
