from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Payment(db.Model):
  __tablename__ = 'payments'
  id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  amount: float = db.Column(db.Float, nullable=False)
  status: str = db.Column(db.String(120), nullable=False)
  payment_method: str = db.Column(db.String(120), nullable=False)
  payment_date: str = db.Column(db.String(120), nullable=False)
  transaction_id: int = db.Column(db.Integer, nullable=False)
  #Relacion con order
  order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
  order = db.relationship("Order", back_populates="payments")
