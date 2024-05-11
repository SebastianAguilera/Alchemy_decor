"""
from app import db
from dataclasses import dataclass

@dataclass
class CartProduct(db.Model):
    __tablename__ = 'cart_product'

    #relacion con producto
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    product = db.relationship("Product", back_populates="carts")

    #relacion con carrito
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), primary_key=True)
    cart = db.relationship("Cart", back_populates="products")
"""


