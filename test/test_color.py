import unittest
from flask import current_app
from app import create_app, db
from app.models import Color

class ColorTestCase(unittest.TestCase):

    def setUp(self):
        self.NAME_PRUEBA = 'Red'
        self.DESCRIPTION_PRUEBA = 'Bright red color'

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
        color = self.__get_color()
        self.assertEqual(color.name, self.NAME_PRUEBA)
        self.assertEqual(color.description, self.DESCRIPTION_PRUEBA)

    def test_color_save(self):
        color = self.__get_color()
        color.save()

        self.assertGreaterEqual(color.id, 1)
        self.assertEqual(color.name, self.NAME_PRUEBA)
        self.assertEqual(color.description, self.DESCRIPTION_PRUEBA)

    def test_color_delete(self):
        color = self.__get_color()
        color.save()
        color_id = color.id

        color.delete()

        self.assertIsNone(Color.find(color_id))

    def test_color_all(self):
        color1 = self.__get_color()
        color2 = self.__get_color()
        color1.save()
        color2.save()

        colors = Color.all()
        self.assertGreaterEqual(len(colors), 2)

    def test_color_find(self):
        color = self.__get_color()
        color.save()

        color_find = Color.find(color.id)
        self.assertIsNotNone(color_find)
        self.assertEqual(color_find.id, color.id)
        self.assertEqual(color_find.name, color.name)
        self.assertEqual(color_find.description, color.description)

    def __get_color(self):
        color = Color()
        color.name = self.NAME_PRUEBA
        color.description = self.DESCRIPTION_PRUEBA
        return color

if __name__ == '__main__':
    unittest.main()
