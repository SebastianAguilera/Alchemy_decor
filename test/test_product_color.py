import unittest
from flask import current_app
from app import create_app, db
from app.models import Product, Color, ProductColor
from app.services import ProductColorService, ProductService, ColorService

class ProductColorTestCase(unittest.TestCase):
  def setUp(self) -> None:
    self.PRODUCT_NAME = 'Oak Table'
    self.PRODUCT_DESCRIPTION = 'A sturdy oak table, 2x1m'
    self.PRODUCT_PRICE = 700.00
    self.COLOR_NAME = 'Red'
    self.COLOR_DESCRIPTION = 'Bright red color'
    self.STOCK = 10
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()
    self.product_services = ProductService()
    self.color_services = ColorService()
    self.product_color_services = ProductColorService()

  def tearDown(self) -> None:
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_app(self):
    self.assertIsNotNone(current_app)
  
  def test_product_color(self):
    product_color, product, color = self.__get_product_color()
    self.assertEqual(product_color.product_id, product.id)
    self.assertEqual(product_color.color_id, color.id)
    self.assertEqual(product_color.stock, self.STOCK)

  def test_product_color_save(self):
    product_color, product, color = self.__get_product_color()
    saved_product_color = self.product_color_services.save(product_color)
    self.assertEqual(saved_product_color.product_id, product.id)
    self.assertEqual(saved_product_color.color_id, color.id)
    self.assertEqual(saved_product_color.stock, self.STOCK)

  def test_product_color_find(self):
    product_color, product, color = self.__get_product_color()
    saved_product_color = self.product_color_services.save(product_color)
    self.assertIsNotNone(self.product_color_services.find(saved_product_color.product_id, saved_product_color.color_id))


  def test_product_color_delete(self):
    product_color, product, color = self.__get_product_color()
    saved_product_color = self.product_color_services.save(product_color)
    self.product_color_services.delete(saved_product_color.product_id, saved_product_color.color_id)
    self.assertIsNone(self.product_color_services.find(saved_product_color.product_id, saved_product_color.color_id))

  def test_product_color_update_stock(self):
    product_color, product, color = self.__get_product_color()
    saved_product_color = self.product_color_services.save(product_color)
    new_stock = 20
    self.product_color_services.update_stock(product.id, color.id, new_stock)
    self.assertEqual(saved_product_color.stock, new_stock)  

  def __get_product_color(self):
    product = self.__create_product()
    color = self.__create_color()
    product_color = ProductColor()
    product_color.product_id = product.id
    product_color.color_id = color.id
    product_color.stock = self.STOCK
    return product_color, product, color

  def __create_product(self):
    product = Product()
    product.name = self.PRODUCT_NAME
    product.description = self.PRODUCT_DESCRIPTION
    product.price = self.PRODUCT_PRICE
    return self.product_services.save(product)

  def __create_color(self):
    color = Color()
    color.name = self.COLOR_NAME
    color.description = self.COLOR_DESCRIPTION
    return self.color_services.save(color)
  
if __name__ == '__main__':
    unittest.main()