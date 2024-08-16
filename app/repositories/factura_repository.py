from typing import List
from app.models import Factura
from app import db

class FacturaRepository:

    def save(self, factura: Factura) -> Factura:
        db.session.add(factura)
        db.session.commit()
        return factura

    def update(self, factura: Factura, id: int) -> Factura:
        entity = self.find(id)
        if entity:
            entity.number = factura.number
            entity.date = factura.date
            entity.total = factura.total
            db.session.commit()
        return entity

    def delete(self, factura: Factura) -> None:
        db.session.delete(factura)
        db.session.commit()

    def all(self) -> List[Factura]:
        return db.session.query(Factura).all()

    def find(self, id: int) -> Factura:
        return db.session.query(Factura).filter(Factura.id == id).one_or_none()

    def find_by_number(self, number: str) -> Factura:
        return db.session.query(Factura).filter(Factura.number == number).one_or_none()
