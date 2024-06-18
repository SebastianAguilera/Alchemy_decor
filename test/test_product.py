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

      product.name = 'silla'
      product.description = 'test'
      product.price = 700.5
      product.stock = 10

      self.assertEqual(product.name, 'silla')
      self.assertEqual(product.description, 'test')
      self.assertEqual(product.price, 700.5)
      self.assertEqual(product.stock, 10)

  def test_product_save(self):
      product = Product()

      product.name = 'silla'
      product.description = 'test'
      product.price = 700.5
      product.stock = 10

      product.save()
      self.assertGreaterEqual(product.id, 1)
      self.assertEqual(product.name, 'silla')
      self.assertEqual(product.description, 'test')
      self.assertEqual(product.price, 700.5)
      self.assertEqual(product.stock, 10)

  def test_product_delete(self):
      product = Product()

      product.name = 'silla'
      product.description = 'test'
      product.price = 700.5
      product.stock = 10

      product.save()

      #borro el producto
      product.delete()
      self.assertIsNone(Product.find(product.id))

  def test_product_all(self):
      product = Product()

      product.name = 'silla'
      product.description = 'test'
      product.price = 700.5
      product.stock = 10

      product.save()

      products = Product.all()
      self.assertGreaterEqual(len(products), 1)

  def test_product_find(self):
      product = Product()

      product.name = 'silla'
      product.description = 'test'
      product.price = 700.5
      product.stock = 10

      product.save()

      product_find = Product.find(product.id)
      self.assertIsNotNone(product_find)
      self.assertEqual(product_find.id, product.id)
      self.assertEqual(product_find.name, product.name)
      self.assertEqual(product_find.description, product.description)
      self.assertEqual(product_find.price, product.price)
      self.assertEqual(product_find.stock, product.stock)

if __name__ == '__main__':
    unittest.main()
