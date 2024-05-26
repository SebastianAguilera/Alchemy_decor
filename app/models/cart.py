"""
from app import db
from dataclasses import dataclass

@dataclass
class Cart(db.Model):
    __tablename__ = 'carts'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state: str = db.Column(db.String(120), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    #relacion con productos
    products = db.relationship("Product", secondary="cart_product", back_populates="carts")
""" 