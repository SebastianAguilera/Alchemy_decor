from app.models import ProductColor
from typing import List
from app import db

class ProductColorRepository:

    def save(self, product_color: ProductColor) -> ProductColor:
        db.session.add(product_color)
        db.session.commit()
        return product_color

    def find(self, product_id: int, color_id: int) -> ProductColor:
        return db.session.query(ProductColor).filter_by(product_id=product_id, color_id=color_id).first()

    def update_stock(self, product_id: int, color_id: int, new_stock: int) -> ProductColor:
        entity = self.find(product_id, color_id)
        if entity:
            entity.stock = new_stock
            db.session.commit()
        return entity

    def delete(self, product_id: int, color_id: int) -> None:
        entity = self.find(product_id, color_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
