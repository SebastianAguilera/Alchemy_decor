import unittest
from flask import current_app
from app import create_app


class HomeResourceTestCase(unittest.TestCase):
  def setUp(self) -> None:
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()

  def tearDown(self) -> None:
    self.app_context.pop()

  def test_index(self):
    #test_client() simula solicitudes HTTP
    client = self.app.test_client(use_cookies=True)
    response = client.get('http://localhost:5000/api/v1/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'ok', response.data)

if __name__ == '__main__':
  unittest.main()


  