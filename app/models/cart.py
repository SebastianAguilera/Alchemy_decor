from dataclasses import dataclass
from app import db

@dataclass
class Cart(db.Model):
    __tablename__ = 'cart'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart: str = db.Column(db.String(120), nullable=False)
    state: str = db.Column(db.String(120), nullable=False)
    deprice: str = db.Column(db.String(120), nullable=False)

"""

    products = db.relationship("Product", secondary="cart_product", back_populates="carts")

"""