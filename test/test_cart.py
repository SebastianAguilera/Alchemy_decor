import unittest
from flask import current_app
from app import create_app, db
from app.models import Cart

class CartTestCase(unittest.TestCase):

    def setUp(self):
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
        cart = Cart(cart='MyCart', state='active', deprice='50')
        self.assertEqual(cart.cart, 'MyCart')
        self.assertEqual(cart.state, 'active')
        self.assertEqual(cart.deprice, '50')

    def test_cart_save(self):
        cart = Cart(cart='MyCart', state='active', deprice='50')
        cart.save()

        self.assertGreaterEqual(cart.id, 1)
        self.assertEqual(cart.cart, 'MyCart')
        self.assertEqual(cart.state, 'active')
        self.assertEqual(cart.deprice, '50')

    def test_cart_delete(self):
        cart = Cart(cart='MyCart', state='active', deprice='50')
        cart.save()
        cart_id = cart.id

        cart.delete()

        self.assertIsNone(Cart.find(cart_id))

    def test_cart_all(self):
        cart1 = Cart(cart='Cart1', state='active', deprice='50')
        cart2 = Cart(cart='Cart2', state='inactive', deprice='100')
        cart1.save()
        cart2.save()

        carts = Cart.all()
        self.assertGreaterEqual(len(carts), 2)

    def test_cart_find(self):
        cart = Cart(cart='MyCart', state='active', deprice='50')
        cart.save()

        cart_find = Cart.find(cart.id)
        self.assertIsNotNone(cart_find)
        self.assertEqual(cart_find.id, cart.id)
        self.assertEqual(cart_find.cart, cart.cart)
        self.assertEqual(cart_find.state, cart.state)
        self.assertEqual(cart_find.deprice, cart.deprice)

if __name__ == '__main__':
    unittest.main()
