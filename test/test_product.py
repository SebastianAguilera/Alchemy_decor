import unittest
from flask import current_app
from app import create_app, db
from app.models import Product
from app.services import ProductService

class ProductTestCase(unittest.TestCase):

  def setUp(self):
    self.NAME_PRUEBA = 'silla'
    self.DESCRIPTION_PRUEBA = 'test'
    self.PRICE_PRUEBA = 700.5
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()
    self.product_services = ProductService()
    
  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_app(self):
    self.assertIsNotNone(current_app)

  def test_product(self):
    product = self.__get_product()

    self.assertEqual(product.name, self.NAME_PRUEBA)
    self.assertEqual(product.description, self.DESCRIPTION_PRUEBA)
    self.assertEqual(product.price, self.PRICE_PRUEBA)


  def test_product_save(self):
    product = self.__get_product()
    saved_product=self.product_services.save(product)
    self.assertGreaterEqual(saved_product.id, 1)
    self.assertEqual(saved_product.name, self.NAME_PRUEBA)
    self.assertEqual(saved_product.description, self.DESCRIPTION_PRUEBA)
    self.assertEqual(saved_product.price, self.PRICE_PRUEBA)

  def test_product_delete(self):
    product = self.__get_product()
    saved_product=self.product_services.save(product)

    self.product_services.delete(saved_product)
    self.assertIsNone(self.product_services.find(saved_product))

  def test_product_all(self):
    product = self.__get_product()
    self.product_services.save(product)
    products = self.product_services.all()
    self.assertGreaterEqual(len(products), 1)

  def test_product_find(self):
    product = self.__get_product()
    self.product_services.save(product)
    product_find = self.product_services.find(1)
    self.assertIsNotNone(product_find)
    self.assertEqual(product_find.id, product.id)
    self.assertEqual(product_find.name, product.name)
    self.assertEqual(product_find.description, product.description)
    self.assertEqual(product_find.price, product.price)

  def __get_product(self): 
    product = Product()
    product.name = self.NAME_PRUEBA
    product.description = self.DESCRIPTION_PRUEBA
    product.price = self.PRICE_PRUEBA
    return product

if __name__ == '__main__':
    unittest.main()
