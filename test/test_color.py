import unittest
from flask import current_app
from app import create_app, db
from app.models import Color
from app.services.color_service import ColorService

class ColorTestCase(unittest.TestCase):

    def setUp(self):
        self.COLOR_NAME = 'leon'
        self.COLOR_DESCRIPTION = 'amarillito tirando a marroncito'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.color_service = ColorService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_color(self):
        color = self.__get_color()
        self.assertEqual(color.name, self.COLOR_NAME)
        self.assertEqual(color.description, self.COLOR_DESCRIPTION)

    def test_color_save(self):
        color = self.__get_color()
        saved_color = self.color_service.save(color)

        self.assertGreaterEqual(saved_color.id, 1)
        self.assertEqual(saved_color.name, self.COLOR_NAME)
        self.assertEqual(saved_color.description, self.COLOR_DESCRIPTION)

    def test_color_delete(self):
        color = self.__get_color()
        saved_color = self.color_service.save(color)
        color_id = saved_color.id
        self.color_service.delete(saved_color)
        self.assertIsNone(self.color_service.find(color_id))

    def test_color_all(self):
        color1 = self.__get_color()
        color2 = self.__get_color()
        self.color_service.save(color1)
        self.color_service.save(color2)

        colors = self.color_service.all()
        self.assertGreaterEqual(len(colors), 2)

    def test_color_find(self):
        color = self.__get_color()
        saved_color = self.color_service.save(color)

        color_found = self.color_service.find(saved_color.id)
        self.assertIsNotNone(color_found)
        self.assertEqual(color_found.id, saved_color.id)
        self.assertEqual(color_found.name, saved_color.name)
        self.assertEqual(color_found.description, saved_color.description)

    def test_color_update(self):
        color = self.__get_color()
        saved_color = self.color_service.save(color)
        new_color = Color(name="Red", description="Bright red color")
        self.color_service.update(new_color, saved_color.id)
        self.assertIsNotNone(self.color_service.find(saved_color.id))
        self.assertEqual(saved_color.id, 1)
        self.assertEqual(saved_color.name, new_color.name)
        self.assertEqual(saved_color.description, new_color.description)

    def __get_color(self):
        color = Color()
        color.name = self.COLOR_NAME
        color.description = self.COLOR_DESCRIPTION
        return color

if __name__ == '__main__':
    unittest.main()
