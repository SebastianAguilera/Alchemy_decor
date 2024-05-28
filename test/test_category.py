import unittest
from flask import current_app
from app import create_app, db
from app.models import Category

class CategoryTestCase(unittest.TestCase):

  def setUp(self):
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()
    
  def tearDown(self):
    self.app_context.pop()

  def test_app(self):
      self.assertIsNotNone(current_app)

  def test_category(self):
      category = Category()
      category.id = 7
      category.name = 'test'
      category.description = 'test test test'
      self.assertEqual(category.id, 7)
      self.assertEqual(category.name, 'test')
      self.assertEqual(category.description, 'test test test')

if __name__ == '__main__':
    unittest.main()
