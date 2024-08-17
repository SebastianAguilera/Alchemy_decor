from typing import List
from app.models import Invoice
from app import db

class InvoiceRepository:

    def save(self, factura: Invoice) -> Invoice:
        db.session.add(factura)
        db.session.commit()
        return factura

    def update(self, invoice: Invoice, id: int) -> Invoice:
        entity = self.find(id)
        if entity:
            entity.number = invoice.number
            entity.date = invoice.date
            entity.total = invoice.total
            db.session.commit()
        return entity

    def delete(self, invoice: Invoice) -> None:
        db.session.delete(invoice)
        db.session.commit()

    def all(self) -> List[Invoice]:
        return db.session.query(Invoice).all()

    def find(self, id: int) -> Invoice:
        return db.session.query(Invoice).filter(Invoice.id == id).one_or_none()

    def find_by_number(self, number: str) -> Invoice:
        return db.session.query(Invoice).filter(Invoice.number == number).one_or_none()
