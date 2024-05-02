from app import db
from dataclasses import dataclass

@dataclass
class Product(db.Model):
    __tablename__ = 'product'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    price: str = db.Column(db.String(120), nullable=False)
    category_id = db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
    product = db.relationship("Product", back_populates='product', uselist=False)

