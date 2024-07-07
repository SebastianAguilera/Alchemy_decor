from typing import List#, Type
from app.models import Category
from app import db

class CategoryRepository:

  def save(self, category: Category) -> Category:
    db.session.add(category)
    db.session.commit()
    return category

  def update(self, category: Category, id: int) -> Category:
    entity = self.find(id)
    entity.name = category.name
    entity.description = category.description
    db.session.add(entity)
    db.session.commit()
    return entity

  def delete(self, category: Category) -> None:
    db.session.delete(category)
    db.session.commit()

  def all(self) -> List[Category]:
    categories = db.session.query(Category).all()
    return categories

  def find(self, id: int) -> Category:
    if id is None or id == 0:
      return None 
    try:
      return db.session.query(Category).filter(Category.id == id).one()
    except:
      return None

  def find_by_name(self, name: str) -> Category: 
    return db.session.query(Category).filter(Category.name == name).one_or_none()
