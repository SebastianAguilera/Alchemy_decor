from app import db
from dataclasses import dataclass

@dataclass
class Color(db.Model):
    __tablename__ = 'color'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color_name: str = db.Column(db.String(120), nullable=False)
    color = db.relationship("Color", back_populates='color', uselist=False)