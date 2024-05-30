import unittest
from flask import current_app
from app import create_app, db
from app.models import Cart

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_cart(self):
        cart = Cart()
        cart.cart = 'MyCart'
        cart.state = 'active'
        cart.deprice = '50'

        self.assertEqual(cart.cart, 'MyCart')
        self.assertEqual(cart.state, 'active')
        self.assertEqual(cart.deprice, '50')

if __name__ == '__main__':
    unittest.main()
