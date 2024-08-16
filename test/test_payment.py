import unittest
from flask import current_app
from app import create_app, db
from app.models import Payment
from app.services import PaymentService

payment_service = PaymentService()

class PaymentTestCase(unittest.TestCase):

  def setUp(self):
    self.AMOUNT_PRUEBA = 700.5
    self.STATUS_PRUEBA = 'test'
    self.PAYMENTH_METOD_PRUEBA = 'test'
    self.PAYMENTH_DATE_PRUEBA = 'test/test/test'
    self.TRANSACTION_ID_PRUEBA = 3


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

  def test_payment(self):
    payment = self.__get_payment()

    self.assertEqual(payment.amount, self.AMOUNT_PRUEBA)
    self.assertEqual(payment.status, self.STATUS_PRUEBA)
    self.assertEqual(payment.payment_method, self.PAYMENTH_METOD_PRUEBA)
    self.assertEqual(payment.payment_date, self.PAYMENTH_DATE_PRUEBA)
    self.assertEqual(payment.transaction_id, self.TRANSACTION_ID_PRUEBA)

  def test_payment_save(self):
    payment = self.__get_payment()
    payment_service.save(payment)

    self.assertGreaterEqual(payment.id, 1)
    self.assertEqual(payment.amount, self.AMOUNT_PRUEBA)
    self.assertEqual(payment.status, self.STATUS_PRUEBA)
    self.assertEqual(payment.payment_method, self.PAYMENTH_METOD_PRUEBA)
    self.assertEqual(payment.payment_date, self.PAYMENTH_DATE_PRUEBA)
    self.assertEqual(payment.transaction_id, self.TRANSACTION_ID_PRUEBA)


  def test_payment_delete(self):
    payment = self.__get_payment()
    payment_service.save(payment)

    payment_service.delete(payment)
    self.assertIsNone(payment_service.find(payment))

  def test_payment_all(self):
    payment = self.__get_payment()
    payment_service.save(payment)

    payments = payment_service.all()
    self.assertGreaterEqual(len(payments), 1)

  def test_payment_find(self):
    payment = self.__get_payment()
    payment_service.save(payment)

    payment_find = payment_service.find(1)
    self.assertIsNotNone(payment_find)
    self.assertEqual(payment_find.id, payment.id)
    self.assertEqual(payment_find.amount, payment.amount)
    self.assertEqual(payment_find.status, payment.status)
    self.assertEqual(payment_find.payment_method, payment.payment_method)
    self.assertEqual(payment_find.payment_date, payment.payment_date)
    self.assertEqual(payment_find.transaction_id, payment.transaction_id)

  def __get_payment(self): 
    payment = Payment()
    payment.amount = self.AMOUNT_PRUEBA
    payment.status = self.STATUS_PRUEBA
    payment.payment_method = self.PAYMENTH_METOD_PRUEBA
    payment.payment_date = self.PAYMENTH_DATE_PRUEBA
    payment.transaction_id = self.TRANSACTION_ID_PRUEBA
    return payment

if __name__ == '__main__':
    unittest.main()