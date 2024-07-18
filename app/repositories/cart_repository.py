from typing import List
from app.models import Cart
from app import db

class CartRepository:

    def save(self, cart: Cart) -> Cart:
        db.session.add(cart)
        db.session.commit()
        return cart

    def update(self, cart: Cart, id: int) -> Cart:
        entity = self.find(id)
        entity.cart = cart.cart
        entity.state = cart.state
        entity.deprice = cart.deprice
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, cart: Cart) -> None:
        db.session.delete(cart)
        db.session.commit()

    def all(self) -> List[Cart]:
        carts = db.session.query(Cart).all()
        return carts

    def find(self, id: int) -> Cart:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Cart).filter(Cart.id == id).one()
        except:
            return None
