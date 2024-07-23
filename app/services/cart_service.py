from app.models import Cart
from app.repositories import CartRepository
from typing import List

class CartService:
    def __init__(self):
        self.repository = CartRepository()

    def save(self, cart: Cart) -> Cart:
        return self.repository.save(cart)

    def update(self, cart: Cart, id: int) -> Cart:
        return self.repository.update(cart, id)

    def delete(self, cart: Cart) -> None:
        self.repository.delete(cart)

    def all(self) -> List[Cart]:
        return self.repository.all()

    def find(self, id: int) -> Cart:
        return self.repository.find(id)
