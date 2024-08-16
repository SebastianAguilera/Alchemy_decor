from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Factura(db.Model):
    __tablename__ = 'facturas'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number: str = db.Column(db.String(120), nullable=False)
    date: str = db.Column(db.String(120), nullable=False)
    total: float = db.Column(db.Float, nullable=False)
    # Relación con la entidad Cart
    carts = db.relationship("Cart", secondary="factura_cart", back_populates="facturas")

    def __init__(self, number: str, date: str, total: float):
        self.number = number
        self.date = date
        self.total = total
