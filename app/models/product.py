from app import db
from dataclasses import dataclass

@dataclass
class Product(db.Model):
    __tablename__ = 'products'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    price: str = db.Column(db.String(120), nullable=False) #Capaz deberia ser Integer para realizar operaciones con el precio
    colors = db.relationship("Color", secundary="product_color", back_populates="products")
