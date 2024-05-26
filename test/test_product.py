


"""

import unittest
from flask import current_app
from app import create_app
from app.models import Product

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.NAME_PRUEBA = 'mesa de roble'
        self.DESCRIPTION_PRUEBA = 'mesa de 2x1m, color marrón, 6 patas'
        self.PRICE_PRUEBA = '70000'
        self.COLORS_PRUEBA = 'marrón oscuro'
        
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_product(self):
        product = self.__get_product()
        self.assertTrue(product.name, self.NAME_PRUEBA)
        self.assertTrue(product.description, self.DESCRIPTION_PRUEBA)
        self.assertTrue(product.price, self.PRICE_PRUEBA)
        self.assertTrue(product.colors, self.COLORS_PRUEBA)
    

    def test_product_save(self):
        
        product = self.__get_product()

        product.save()
        self.assertGreaterEqual(product.id, 1)
        self.assertTrue(product.name, self.NAME_PRUEBA)
        self.assertTrue(product.description(self.DESCRIPTION_PRUEBA))
        self.assertTrue(product.price, self.PRICE_PRUEBA)
        self.assertTrue(product.colors, self.COLORS_PRUEBA)
    
    def test_product_delete(self):
        product = self.__get_product()
        product.save()

        #borro el usuario
        product.delete()
        self.assertIsNone(product.find(product.id))
    
    
    def __get_product(self):
        return Product(
            name=self.NAME_PRUEBA,
            description=self.DESCRIPTION_PRUEBA,
            price=self.PRICE_PRUEBA,
            colors=self.COLORS_PRUEBA
        )

if __name__ == '__main__':
    unittest.main()

"""