import unittest
from flask import current_app
from app import create_app, db
from app.models import Color

class ColorTestCase(unittest.TestCase):

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

    def test_color(self):
        color = Color(name='Red', description='Bright red color')
        self.assertEqual(color.name, 'Red')
        self.assertEqual(color.description, 'Bright red color')

    def test_color_save(self):
        color = Color(name='Red', description='Bright red color')
        color.save()

        self.assertGreaterEqual(color.id, 1)
        self.assertEqual(color.name, 'Red')
        self.assertEqual(color.description, 'Bright red color')

    def test_color_delete(self):
        color = Color(name='Red', description='Bright red color')
        color.save()
        color_id = color.id

        color.delete()

        self.assertIsNone(Color.find(color_id))

    def test_color_all(self):
        color1 = Color(name='Red', description='Bright red color')
        color2 = Color(name='Blue', description='Deep blue color')
        color1.save()
        color2.save()

        colors = Color.all()
        self.assertGreaterEqual(len(colors), 2)

    def test_color_find(self):
        color = Color(name='Red', description='Bright red color')
        color.save()

        color_find = Color.find(color.id)
        self.assertIsNotNone(color_find)
        self.assertEqual(color_find.id, color.id)
        self.assertEqual(color_find.name, color.name)
        self.assertEqual(color_find.description, color.description)

if __name__ == '__main__':
    unittest.main()
