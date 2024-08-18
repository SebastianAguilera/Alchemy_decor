from app import db
from dataclasses import dataclass

@dataclass
class OrderProduct(db.Model):
  __tablename__ = 'order_product'

  product_id : int = db.Column(db.Integer, db.ForeignKey("products.id"), primary_key = True)
  order_id : int = db.Column(db.Integer, db.ForeignKey("orders.id"), primary_key = True)


  product = db.relationship("Product", back_populates="order_products")
  order = db.relationship("Order", back_populates="product_orders")