import unittest
from flask import current_app
from app import create_app, db
from app.models import Product

class ProductTestCase(unittest.TestCase):

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

  def test_product(self):
      product = Product()
      product.id = 10
      product.name = 'silla'
      product.description = 'test'
      product.price = 700.5
      product.stock = 10

      self.assertEqual(product.id, 10)
      self.assertEqual(product.name, 'silla')
      self.assertEqual(product.description, 'test')
      self.assertEqual(product.price, 700.5)
      self.assertEqual(product.stock, 10)

if __name__ == '__main__':
    unittest.main()
