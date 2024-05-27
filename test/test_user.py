import unittest
from flask import current_app
from app import create_app
from app.models import User, UserData


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
    self.assertEqual(user.email, 'test@test.com')
    self.assertEqual(user.username, 'test')
    self.assertEqual(user.password, 'test1234')

  def test_user_data(self):
    user = User()
    user.email = 'test@test.com'
    user.username = 'test'
    user.password = 'test1234'

    data = UserData()
    data.surname = 'surname'
    data.address = 'address 1234'
    data.city = 'city'
    data.country = 'country'
    data.phone = '542605502105'
    user.user_data = data

    self.assertIsNotNone(user.user_data)
    self.assertEqual(user.user_data.surname, 'surname')
    self.assertEqual(user.user_data.address, 'address 1234')
    self.assertEqual(user.user_data.phone, '542605502105')
    self.assertEqual(user.user_data.city, 'city')
    self.assertEqual(user.user_data.country,'country')

if __name__ == '__main__':
    unittest.main()
