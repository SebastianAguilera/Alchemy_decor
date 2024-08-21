import unittest
from flask import current_app
from app import create_app, db
from app.models import User, UserData
from app.services import UserService

user_service = UserService()

class UserTestCase(unittest.TestCase):


  def setUp(self):
    self.USERNAME_PRUEBA = 'username'
    self.EMAIL_PRUEBA = 'email'
    self.PASSWORD_PRUEBA = 'password123'
    self.FIRSTNAME_PRUEBA = 'firstname'
    self.LASTNAME_PRUEBA = 'lastname'
    self.PHONE_PRUEBA = '1234567890'
    self.ADDRESS_PRUEBA = 'address'
    self.CITY_PRUEBA = 'city'
    self.COUNTRY_PRUEBA = 'country'
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
    user = self.__get_user()
    self.assertEqual(user.email, self.EMAIL_PRUEBA)
    self.assertEqual(user.username, self.USERNAME_PRUEBA)
    self.assertTrue(user.password, self.PASSWORD_PRUEBA)
    self.assertIsNotNone(user.data)
    self.assertEqual(user.data.firstname, self.FIRSTNAME_PRUEBA)
    self.assertEqual(user.data.lastname, self.LASTNAME_PRUEBA)
    self.assertEqual(user.data.phone, self.PHONE_PRUEBA)
    self.assertEqual(user.data.address, self.ADDRESS_PRUEBA)
    self.assertEqual(user.data.city, self.CITY_PRUEBA)
    self.assertEqual(user.data.country, self.COUNTRY_PRUEBA)


  def test_user_save(self):
    user = self.__get_user()
    user_service.save(user)
    self.assertGreaterEqual(user.id, 1)
    self.assertEqual(user.email, self.EMAIL_PRUEBA)
    self.assertEqual(user.username, self.USERNAME_PRUEBA)
    self.assertIsNotNone(user.password)
    self.assertTrue(user_service.check_auth(user.username, self.PASSWORD_PRUEBA))
    self.assertIsNotNone(user.data)
    self.assertEqual(user.data.firstname, self.FIRSTNAME_PRUEBA)
    self.assertEqual(user.data.lastname, self.LASTNAME_PRUEBA)
    self.assertEqual(user.data.phone, self.PHONE_PRUEBA)
    self.assertEqual(user.data.address, self.ADDRESS_PRUEBA)
    self.assertEqual(user.data.city, self.CITY_PRUEBA)
    self.assertEqual(user.data.country, self.COUNTRY_PRUEBA)

  def test_user_delete(self):
    user = self.__get_user()
    user_service.save(user)

    user_service.delete(user.id)
    self.assertIsNone(user_service.find(user))

  def test_user_all(self):
    user = self.__get_user()
    user_service.save(user)
    users = user_service.all()
    self.assertGreaterEqual(len(users), 1)

  def test_user_find(self):
    user = self.__get_user()
    user_service.save(user)
    user_find = user_service.find(1)
    self.assertIsNotNone(user_find)
    self.assertEqual(user_find.id, user.id)
    self.assertEqual(user_find.email, user.email)

  def test_user_find_by_username(self):
    user = self.__get_user()
    user_service.save(user)
    username = self.USERNAME_PRUEBA
    user_found = user_service.find_by_username(username)
    self.assertIsNotNone(user_found)
    self.assertEqual(user_found.id, user.id)

  def test_user_find_by_email(self):
    user = self.__get_user()
    user_service.save(user)
    email = self.EMAIL_PRUEBA
    user_found = user_service.find_by_email(email)
    self.assertIsNotNone(user_found)

  def __get_user(self): 
    data = UserData()
    data.firstname = self.FIRSTNAME_PRUEBA
    data.lastname = self.LASTNAME_PRUEBA
    data.phone = self.PHONE_PRUEBA
    data.address = self.ADDRESS_PRUEBA
    data.city = self.CITY_PRUEBA
    data.country = self.COUNTRY_PRUEBA
    user = User()
    user.username = self.USERNAME_PRUEBA
    user.email = self.EMAIL_PRUEBA
    user.password = self.PASSWORD_PRUEBA
    user.data = data
    return user

if __name__ == '__main__':
    unittest.main()
 