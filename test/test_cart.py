import unittest
from flask import current_app
from app import create_app, db
from app.models import Cart

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.CART_PRUEBA = 'MyCart'
        self.STATE_PRUEBA = 'active'
        self.DEPRICE_PRUEBA = '50'

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_cart(self):
        cart = self.__get_cart()
        self.assertEqual(cart.cart, self.CART_PRUEBA)
        self.assertEqual(cart.state, self.STATE_PRUEBA)
        self.assertEqual(cart.deprice, self.DEPRICE_PRUEBA)

    def test_cart_save(self):
        cart = self.__get_cart()
        cart.save()

        self.assertGreaterEqual(cart.id, 1)
        self.assertEqual(cart.cart, self.CART_PRUEBA)
        self.assertEqual(cart.state, self.STATE_PRUEBA)
        self.assertEqual(cart.deprice, self.DEPRICE_PRUEBA)

    def test_cart_delete(self):
        cart = self.__get_cart()
        cart.save()
        cart_id = cart.id

        cart.delete()

        self.assertIsNone(Cart.find(cart_id))

    def test_cart_all(self):
        cart1 = self.__get_cart()
        cart2 = self.__get_cart()
        cart1.save()
        cart2.save()

        carts = Cart.all()
        self.assertGreaterEqual(len(carts), 2)

    def test_cart_find(self):
        cart = self.__get_cart()
        cart.save()

        cart_find = Cart.find(cart.id)
        self.assertIsNotNone(cart_find)
        self.assertEqual(cart_find.id, cart.id)
        self.assertEqual(cart_find.cart, cart.cart)
        self.assertEqual(cart_find.state, cart.state)
        self.assertEqual(cart_find.deprice, cart.deprice)

    def __get_cart(self):
        cart = Cart()
        cart.cart = self.CART_PRUEBA
        cart.state = self.STATE_PRUEBA
        cart.deprice = self.DEPRICE_PRUEBA
        return cart

if __name__ == '__main__':
    unittest.main()
