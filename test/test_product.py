import unittest
from flask import current_app
from app import create_app, db
from app.models.product import Product

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.PRODUCT_ID = 1
        self.PRODUCT_NAME = 'Oak Table'
        self.PRODUCT_DESCRIPTION = 'A sturdy oak table, 2x1m'
        self.PRODUCT_PRICE = 700.00
        self.PRODUCT_STOCK = 10

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_product(self):
        product = Product()
        product.id = self.PRODUCT_ID
        product.name = self.PRODUCT_NAME
        product.description = self.PRODUCT_DESCRIPTION
        product.price = self.PRODUCT_PRICE
        product.stock = self.PRODUCT_STOCK

        self.assertEqual(product.id, self.PRODUCT_ID)
        self.assertEqual(product.name, self.PRODUCT_NAME)
        self.assertEqual(product.description, self.PRODUCT_DESCRIPTION)
        self.assertEqual(product.price, self.PRODUCT_PRICE)
        self.assertEqual(product.stock, self.PRODUCT_STOCK)

if __name__ == '__main__':
    unittest.main()
