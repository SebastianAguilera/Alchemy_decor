from typing import List
from app.models import OrdenDePago
from app import db

class OrdenDePagoRepository:

    def save(self, orden_de_pago: OrdenDePago) -> OrdenDePago:
        db.session.add(orden_de_pago)
        db.session.commit()
        return orden_de_pago

    def update(self, orden_de_pago: OrdenDePago, id: int) -> OrdenDePago:
        entity = self.find(id)
        if entity:
            entity.amount = orden_de_pago.amount
            entity.payment_date = orden_de_pago.payment_date
            entity.status = orden_de_pago.status
            db.session.commit()
        return entity

    def delete(self, orden_de_pago: OrdenDePago) -> None:
        db.session.delete(orden_de_pago)
        db.session.commit()

    def all(self) -> List[OrdenDePago]:
        return db.session.query(OrdenDePago).all()

    def find(self, id: int) -> OrdenDePago:
        return db.session.query(OrdenDePago).filter(OrdenDePago.id == id).one_or_none()

    def find_by_status(self, status: str) -> List[OrdenDePago]:
        return db.session.query(OrdenDePago).filter(OrdenDePago.status == status).all()
