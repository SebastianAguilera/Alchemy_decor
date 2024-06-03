from dataclasses import dataclass
from app import db

@dataclass
class Color(db.Model):
    __tablename__ = 'color'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)

    """
    products = db.relationship("Product", secondary="product_color", back_populates="color")

    """