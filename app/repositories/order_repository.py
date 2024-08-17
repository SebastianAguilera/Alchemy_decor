from typing import List
from app.models.order import Order
from app import db

class OrderRepository:

    def save(self, order: Order) -> Order:
        db.session.add(order)
        db.session.commit()
        return order

    def update(self, order: Order, id: int) -> Order:
        entity = self.find(id)
        if entity:
            entity.amount = order.amount
            entity.payment_date = order.payment_date
            entity.status = order.status
            db.session.commit()
        return entity

    def delete(self, order: Order) -> None:
        db.session.delete(order)
        db.session.commit()

    def all(self) -> List[Order]:
        return db.session.query(Order).all()

    def find(self, id: int) -> Order:
        return db.session.query(Order).filter(Order.id == id).one_or_none()

    def find_by_status(self, status: str) -> List[Order]:
        return db.session.query(Order).filter(Order.status == status).all()
