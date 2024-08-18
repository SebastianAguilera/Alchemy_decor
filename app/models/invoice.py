from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Invoice(db.Model):
    __tablename__ = 'invoices'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number: str = db.Column(db.String(120), nullable=False)
    date: str = db.Column(db.String(120), nullable=False)
    total: float = db.Column(db.Float, nullable=False)
    
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship("Order", back_populates="invoices")

    def __init__(self, number: str, date: str, total: float):
        self.number = number
        self.date = date
        self.total = total
