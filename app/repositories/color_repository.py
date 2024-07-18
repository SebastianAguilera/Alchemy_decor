from typing import List
from app.models import Color
from app import db

class ColorRepository:

    def save(self, color: Color) -> Color:
        db.session.add(color)
        db.session.commit()
        return color

    def update(self, color: Color, id: int) -> Color:
        entity = self.find(id)
        entity.name = color.name
        entity.description = color.description
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, color: Color) -> None:
        db.session.delete(color)
        db.session.commit()

    def all(self) -> List[Color]:
        colors = db.session.query(Color).all()
        return colors

    def find(self, id: int) -> Color:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Color).filter(Color.id == id).one()
        except:
            return None

    def find_by_name(self, name: str) -> Color:
        return db.session.query(Color).filter(Color.name == name).one_or_none()
