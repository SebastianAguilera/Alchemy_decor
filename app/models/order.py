from dataclasses import dataclass
from app import db

@dataclass
class Order(db.Model):
    __tablename__ = 'orders'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount: float = db.Column(db.Float, nullable=False)
    payment_date: str = db.Column(db.String(120), nullable=False)
    status: str = db.Column(db.String(120), nullable=False)
    #Una orden puede tener varias facturas 
    invoices = db.relationship("Invoice", back_populates="order", cascade="all, delete-orphan")
    #Relacion entre orden y producto
    product_orders = db.relationship("OrderProduct", back_populates="order", cascade="all, delete-orphan")
    #Relacion con payment
    payments = db.relationship("Payment", back_populates="order")
    #Relacion con User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="orders")

    def __init__(self, amount: float, payment_date: str, status: str):
        self.amount = amount
        self.payment_date = payment_date
        self.status = status
