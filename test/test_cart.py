import unittest
from flask import current_app
from app import create_app, db
from app.models import Cart
from app.services.cart_service import CartService

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.CART_PRUEBA = 'MyCart'
        self.STATE_PRUEBA = 'active'
        self.DEPRICE_PRUEBA = '50'

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.cart_service = CartService()

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
        saved_cart = self.cart_service.save(cart)

        self.assertGreaterEqual(saved_cart.id, 1)
        self.assertEqual(saved_cart.cart, self.CART_PRUEBA)
        self.assertEqual(saved_cart.state, self.STATE_PRUEBA)
        self.assertEqual(saved_cart.deprice, self.DEPRICE_PRUEBA)

    def test_cart_delete(self):
        cart = self.__get_cart()
        saved_cart = self.cart_service.save(cart)
        cart_id = saved_cart.id

        self.cart_service.delete(saved_cart)

        self.assertIsNone(self.cart_service.find(cart_id))

    def test_cart_all(self):
        cart1 = self.__get_cart()
        cart2 = self.__get_cart()
        self.cart_service.save(cart1)
        self.cart_service.save(cart2)

        carts = self.cart_service.all()
        self.assertGreaterEqual(len(carts), 2)

    def test_cart_find(self):
        cart = self.__get_cart()
        saved_cart = self.cart_service.save(cart)

        cart_find = self.cart_service.find(saved_cart.id)
        self.assertIsNotNone(cart_find)
        self.assertEqual(cart_find.id, saved_cart.id)
        self.assertEqual(cart_find.cart, saved_cart.cart)
        self.assertEqual(cart_find.state, saved_cart.state)
        self.assertEqual(cart_find.deprice, saved_cart.deprice)

    def __get_cart(self):
        cart = Cart()
        cart.cart = self.CART_PRUEBA
        cart.state = self.STATE_PRUEBA
        cart.deprice = self.DEPRICE_PRUEBA
        return cart

if __name__ == '__main__':
    unittest.main()
