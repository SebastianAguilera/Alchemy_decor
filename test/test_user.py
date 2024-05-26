import unittest
from flask import current_app
from app import create_app
from app.models import User


class UserTestCase(unittest.TestCase):

  """
  The setUp() and tearDown() methods allow you to define instructions 
  that will be executed before and after each test method
  """

  def setUp(self):
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()
  def tearDown(self):
    self.app_context.pop()


  def test_app(self):
    self.assertIsNotNone(current_app)
  
  def test_user(self):
    user = User()
    user.email = 'test@test.com'
    user.username = 'test'
    user.password = 'test1234'
    self.assertTrue(user.email, 'test@test.com')
    self.assertTrue(user.username, 'test')
    self.assertTrue(user.password, 'test1234')



if __name__ == '__main__':
    unittest.main()
