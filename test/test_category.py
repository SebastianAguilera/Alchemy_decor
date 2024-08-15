import unittest
from flask import current_app
from app import create_app, db
from app.models import Category
from app.services import CategoryService

category_service = CategoryService()

class CategoryTestCase(unittest.TestCase):

  def setUp(self):
    self.NAME_PRUEBA = 'test'
    self.DESCRIPTION_PRUEBA = 'test test test'

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

  def test_category(self):
      category = self.__get_category()
      
      self.assertEqual(category.name, self.NAME_PRUEBA)
      self.assertEqual(category.description, self.DESCRIPTION_PRUEBA)

  def test_category_save(self):
      category = self.__get_category()
      category_service.save(category)

      self.assertGreaterEqual(category.id, 1)
      self.assertEqual(category.name, 'test')
      self.assertEqual(category.description, 'test test test')

  def test_category_delete(self):
      category = self.__get_category()
      category_service.save(category)
      category_id = category.id

      category_service.delete(category)

      self.assertIsNone(category_service.find(category_id))

  def test_category_all(self):
      category1 = self.__get_category()
      category2 = self.__get_category()
      category_service.save(category1)
      category_service.save(category2)

      categories = category_service.all()
      self.assertGreaterEqual(len(categories), 2)

  def test_category_find(self):
      category = self.__get_category()
      category_service.save(category)

      category_find = category_service.find(1)
      self.assertIsNotNone(category_find)
      self.assertEqual(category_find.id, category.id)
      self.assertEqual(category_find.name, category.name)
      self.assertEqual(category_find.description, category.description)

  
  def test_category_update(self):
      category = self.__get_category()
      saved_category = category_service.save(category)
      new_category = Category(name="mesa", description="4 patas")
      category_service.update(new_category, saved_category.id)
      self.assertIsNotNone(category_service.find(saved_category.id))
      self.assertEqual(saved_category.id, 1)
      self.assertEqual(saved_category.name, new_category.name)
      self.assertEqual(saved_category.description, new_category.description)


  def __get_category(self): 
      category = Category()
      category.name = self.NAME_PRUEBA
      category.description = self.DESCRIPTION_PRUEBA
      return category

if __name__ == '__main__':
    unittest.main()
