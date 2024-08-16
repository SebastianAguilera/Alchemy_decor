import unittest
from flask import current_app
from app import create_app, db
from app.models import OrdenDePago
from app.services.orden_de_pago_service import OrdenDePagoService

class OrdenDePagoTestCase(unittest.TestCase):

    def setUp(self):
        self.AMOUNT_PRUEBA = 150.0
        self.PAYMENT_DATE_PRUEBA = '2024-08-12'
        self.STATUS_PRUEBA = 'pending'

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.orden_de_pago_service = OrdenDePagoService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_orden_de_pago(self):
        orden_de_pago = self.__get_orden_de_pago()
        self.assertEqual(orden_de_pago.amount, self.AMOUNT_PRUEBA)
        self.assertEqual(orden_de_pago.payment_date, self.PAYMENT_DATE_PRUEBA)
        self.assertEqual(orden_de_pago.status, self.STATUS_PRUEBA)

    def test_orden_de_pago_save(self):
        orden_de_pago = self.__get_orden_de_pago()
        saved_orden_de_pago = self.orden_de_pago_service.save(orden_de_pago)

        self.assertGreaterEqual(saved_orden_de_pago.id, 1)
        self.assertEqual(saved_orden_de_pago.amount, self.AMOUNT_PRUEBA)
        self.assertEqual(saved_orden_de_pago.payment_date, self.PAYMENT_DATE_PRUEBA)
        self.assertEqual(saved_orden_de_pago.status, self.STATUS_PRUEBA)

    def test_orden_de_pago_delete(self):
        orden_de_pago = self.__get_orden_de_pago()
        saved_orden_de_pago = self.orden_de_pago_service.save(orden_de_pago)
        orden_de_pago_id = saved_orden_de_pago.id

        self.orden_de_pago_service.delete(saved_orden_de_pago)

        self.assertIsNone(self.orden_de_pago_service.find(orden_de_pago_id))

    def test_orden_de_pago_all(self):
        orden_de_pago1 = self.__get_orden_de_pago()
        orden_de_pago2 = self.__get_orden_de_pago()
        self.orden_de_pago_service.save(orden_de_pago1)
        self.orden_de_pago_service.save(orden_de_pago2)

        ordenes_de_pago = self.orden_de_pago_service.all()
        self.assertGreaterEqual(len(ordenes_de_pago), 2)

    def test_orden_de_pago_find(self):
        orden_de_pago = self.__get_orden_de_pago()
        saved_orden_de_pago = self.orden_de_pago_service.save(orden_de_pago)

        orden_de_pago_find = self.orden_de_pago_service.find(saved_orden_de_pago.id)
        self.assertIsNotNone(orden_de_pago_find)
        self.assertEqual(orden_de_pago_find.id, saved_orden_de_pago.id)
        self.assertEqual(orden_de_pago_find.amount, saved_orden_de_pago.amount)
        self.assertEqual(orden_de_pago_find.payment_date, saved_orden_de_pago.payment_date)
        self.assertEqual(orden_de_pago_find.status, saved_orden_de_pago.status)

    def __get_orden_de_pago(self):
        return OrdenDePago(amount=self.AMOUNT_PRUEBA, payment_date=self.PAYMENT_DATE_PRUEBA, status=self.STATUS_PRUEBA)

if __name__ == '__main__':
    unittest.main()
