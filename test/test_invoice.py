import unittest
from flask import current_app
from app import create_app, db
from app.models import Invoice
from app.services import InvoiceService

class FacturaTestCase(unittest.TestCase):

    def setUp(self):
        self.NUMBER_PRUEBA = '12345'
        self.DATE_PRUEBA = '2024-08-12'
        self.TOTAL_PRUEBA = 100.0

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.factura_service = InvoiceService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_factura(self):
        factura = self.__get_factura()
        self.assertEqual(factura.number, self.NUMBER_PRUEBA)
        self.assertEqual(factura.date, self.DATE_PRUEBA)
        self.assertEqual(factura.total, self.TOTAL_PRUEBA)

    def test_factura_save(self):
        factura = self.__get_factura()
        saved_factura = self.factura_service.save(factura)

        self.assertGreaterEqual(saved_factura.id, 1)
        self.assertEqual(saved_factura.number, self.NUMBER_PRUEBA)
        self.assertEqual(saved_factura.date, self.DATE_PRUEBA)
        self.assertEqual(saved_factura.total, self.TOTAL_PRUEBA)

    def test_factura_delete(self):
        factura = self.__get_factura()
        saved_factura = self.factura_service.save(factura)
        factura_id = saved_factura.id

        self.factura_service.delete(saved_factura)

        self.assertIsNone(self.factura_service.find(factura_id))

    def test_factura_all(self):
        factura1 = self.__get_factura()
        factura2 = self.__get_factura()
        self.factura_service.save(factura1)
        self.factura_service.save(factura2)

        facturas = self.factura_service.all()
        self.assertGreaterEqual(len(facturas), 2)

    def test_factura_find(self):
        factura = self.__get_factura()
        saved_factura = self.factura_service.save(factura)

        factura_find = self.factura_service.find(saved_factura.id)
        self.assertIsNotNone(factura_find)
        self.assertEqual(factura_find.id, saved_factura.id)
        self.assertEqual(factura_find.number, saved_factura.number)
        self.assertEqual(factura_find.date, saved_factura.date)
        self.assertEqual(factura_find.total, saved_factura.total)

    def __get_factura(self):
        return Invoice(number=self.NUMBER_PRUEBA, date=self.DATE_PRUEBA, total=self.TOTAL_PRUEBA)

if __name__ == '__main__':
    unittest.main()
