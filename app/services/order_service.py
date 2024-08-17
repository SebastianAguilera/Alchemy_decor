from typing import List
from app.models.order import Order
from app.repositories.order_repository import OrderRepository

class OrdenDePagoService:
    def __init__(self):
        self.order_repository = OrderRepository()

    def save(self, order: Order) -> Order:
        return self.order_repository.save(order)

    def update(self, order: Order, id: int) -> Order:
        return self.order_repository.update(order, id)

    def delete(self, order: Order) -> None:
        self.order_repository.delete(order)

    def all(self) -> List[Order]:
        return self.order_repository.all()

    def find(self, id: int) -> Order:
        return self.order_repository.find(id)

    def find_by_status(self, status: str) -> List[Order]:
        return self.order_repository.find_by_status(status)
