from app import db
from dataclasses import dataclass

@dataclass
class Category(db.Model):
    __tablename__ = 'categorys'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('users.id'))
    product = db.relationship("Product", back_populates='category')
