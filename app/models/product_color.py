from app import db
from dataclasses import dataclass
from sqlalchemy import CheckConstraint

@dataclass
class ProductColor(db.Model):
    __tablename__ = 'product_color'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'), primary_key=True)
    product = db.relationship("Product", back_populates="colors")
    color = db.relationship("Color", back_populates="products")
    stock : int = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        CheckConstraint('stock >= 0', name='check_stock_non_negative'),
  )
