import unittest
from flask import current_app
from app import create_app, db
from app.models import Role
from app.services.role_service import RoleService

class RoleTestCase(unittest.TestCase):

    def setUp(self):
        self.NAME_PRUEBA = 'Admin'
        self.DESCRIPTION_PRUEBA = 'Administrator role'
        self.service = RoleService()

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_role(self):
        role = self.__get_role()
        self.assertEqual(role.name, self.NAME_PRUEBA)
        self.assertEqual(role.description, self.DESCRIPTION_PRUEBA)

    def test_role_save(self):
        role = self.__get_role()
        self.service.save(role)

        self.assertGreaterEqual(role.id, 1)
        self.assertEqual(role.name, self.NAME_PRUEBA)
        self.assertEqual(role.description, self.DESCRIPTION_PRUEBA)

    def test_role_delete(self):
        role = self.__get_role()
        self.service.save(role)

        # Borrar el rol
        self.service.delete(role)
        self.assertIsNone(self.service.find(role.id))

    def test_role_all(self):
        role = self.__get_role()
        self.service.save(role)

        roles = self.service.all()
        self.assertGreaterEqual(len(roles), 1)

    def test_role_find(self):
        role = self.__get_role()
        self.service.save(role)

        role_find = self.service.find(role.id)
        self.assertIsNotNone(role_find)
        self.assertEqual(role_find.id, role.id)
        self.assertEqual(role_find.name, role.name)
        self.assertEqual(role_find.description, role.description)

    def __get_role(self):
        role = Role(name=self.NAME_PRUEBA, description=self.DESCRIPTION_PRUEBA)
        return role

if __name__ == '__main__':
    unittest.main()
