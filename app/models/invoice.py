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

    def __init__(self, number: str, date: str, total: float):
        self.number = number
        self.date = date
        self.total = total
