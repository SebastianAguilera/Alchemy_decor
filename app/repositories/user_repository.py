from app.models import User
from app import db

class UserRepository:
    def __init__(self):
        self.__model = User

    def get_all(self) -> list[User]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> User:
        return db.session.query(self.__model).get(id)

    def create(self, entity: User) -> User:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, u: User) -> User:
        entity = self.get_by_id(id)
        entity.username = u.username
        entity.email = u.email
        entity.password = u.password
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id)-> bool:
        usuario = self.get_by_id(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario