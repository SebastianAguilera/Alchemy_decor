import unittest
from flask import current_app
from app import create_app, db
from app.models import Category

class CategoryTestCase(unittest.TestCase):

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

  def test_category(self):
      category = Category()
      category.id = 7
      category.name = 'test'
      category.description = 'test test test'
      
      self.assertEqual(category.id, 7)
      self.assertEqual(category.name, 'test')
      self.assertEqual(category.description, 'test test test')

  def test_category_save(self):
        category = Category(name='test', description='test test test')
        category.save()

        self.assertGreaterEqual(category.id, 1)
        self.assertEqual(category.name, 'test')
        self.assertEqual(category.description, 'test test test')

  def test_category_delete(self):
        category = Category(name='test', description='test test test')
        category.save()
        category_id = category.id

        category.delete()

        self.assertIsNone(Category.find(category_id))

  def test_category_all(self):
        category1 = Category(name='test1', description='test test test1')
        category2 = Category(name='test2', description='test test test2')
        category1.save()
        category2.save()

        categories = Category.all()
        self.assertGreaterEqual(len(categories), 2)

  def test_category_find(self):
        category = Category(name='test', description='test test test')
        category.save()

        category_find = Category.find(category.id)
        self.assertIsNotNone(category_find)
        self.assertEqual(category_find.id, category.id)
        self.assertEqual(category_find.name, category.name)
        self.assertEqual(category_find.description, category.description)

if __name__ == '__main__':
    unittest.main()
