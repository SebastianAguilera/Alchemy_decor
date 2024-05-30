import unittest
from flask import current_app
from app import create_app, db
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
    db.create_all()
    
  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_app(self):
    self.assertIsNotNone(current_app)

  
  def test_user(self):
    
    data = UserData()
    data.firstname = 'firstname'
    data.lastname = 'lastname'
    data.phone = '123456789'
    data.address = 'address'
    data.city = 'city'
    data.country = 'country'

    user = User(data)
    user.username = 'test'
    user.email = 'test@test.com'
    user.password = 'test1234'

    self.assertEqual(user.email, 'test@test.com')
    self.assertEqual(user.username, 'test')
    self.assertEqual(user.password, 'test1234')
    self.assertIsNotNone(user.data)
    self.assertEqual(user.data.firstname, 'firstname')
    self.assertEqual(user.data.lastname, 'lastname')
    self.assertEqual(user.data.phone, '123456789')
    self.assertEqual(user.data.address, 'address')
    self.assertEqual(user.data.city, 'city')
    self.assertEqual(user.data.country,'country')

if __name__ == '__main__':
    unittest.main()
 