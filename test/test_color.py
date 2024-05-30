import unittest
from flask import current_app
from app import create_app, db
from app.models import Color

class ColorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_color(self):
        color = Color()
        color.name = 'Red'
        color.description = 'Bright red color'

        self.assertEqual(color.name, 'Red')
        self.assertEqual(color.description, 'Bright red color')

if __name__ == '__main__':
    unittest.main()