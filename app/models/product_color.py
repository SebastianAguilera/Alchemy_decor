from app import db
from dataclasses import dataclass
from .color import Color

@dataclass
class ProductColor(db.Model):
    __tablename__ = 'product_color'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.relationship("Color", back_popilates='color', uselist=False)

    def __init__(self, color: Color = None):
        self.color = color