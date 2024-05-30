import unittest
from flask import current_app
from app import create_app, db
from app.models import Product

class ProductTestCase(unittest.TestCase):

  def setUp(self):
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()
    
  def tearDown(self):
    self.app_context.pop()

  def test_app(self):
      self.assertIsNotNone(current_app)

  def test_product(self):
      product = Product()
      product.id = 10
      product.name = 'test'
      product.description = 'hola'
      product.price = 10.5
      product.stock = 10

      self.assertTrue(product.id, 11)
      self.assertEqual(product.name, 'test')
      self.assertEqual(product.description, 'hola')
      self.assertEqual(product.price, 10.5)
      self.assertEqual(product.stock, 10)

if __name__ == '__main__':
    unittest.main()
