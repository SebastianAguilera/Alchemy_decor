from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class OrdenDePago(db.Model):
    __tablename__ = 'ordenes_de_pago'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount: float = db.Column(db.Float, nullable=False)
    payment_date: str = db.Column(db.String(120), nullable=False)
    status: str = db.Column(db.String(120), nullable=False)
    # Relación con la entidad Factura
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'))
    factura = db.relationship("Factura", back_populates="ordenes_de_pago")

    def __init__(self, amount: float, payment_date: str, status: str, factura=None):
        self.amount = amount
        self.payment_date = payment_date
        self.status = status
        self.factura = factura
