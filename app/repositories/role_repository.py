from typing import List
from app.models import Role
from app import db

class RoleRepository:

    def save(self, role: Role) -> Role:
        db.session.add(role)
        db.session.commit()
        return role

    def update(self, role: Role, id: int) -> Role:
        entity = self.find(id)
        if entity:
            entity.name = role.name
            entity.description = role.description
            db.session.add(entity)
            db.session.commit()
        return entity

    def delete(self, role: Role) -> None:
        db.session.delete(role)
        db.session.commit()

    def all(self) -> List[Role]:
        return db.session.query(Role).all()

    def find(self, id: int) -> Role:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Role).filter(Role.id == id).one()
        except:
            return None

    def find_by_name(self, name: str) -> Role:
        return db.session.query(Role).filter(Role.name == name).one_or_none()
