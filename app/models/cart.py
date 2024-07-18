from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class Cart(db.Model):
    __tablename__ = 'carts'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart: str = db.Column(db.String(120), nullable=False)
    state: str = db.Column(db.String(120), nullable=False)
    deprice: str = db.Column(db.String(120), nullable=False)

