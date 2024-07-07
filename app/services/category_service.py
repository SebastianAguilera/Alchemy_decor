from typing import List
from app.models import Category
from app.repositories import CategoryRepository

repository = CategoryRepository()

class CategoryService:

  def save(self, category: Category) -> Category:
    return repository.save(category)

  def update(self, category: Category, id: int) -> Category:
    return repository.update(category, id)

  def delete(self, category: Category) -> None:
    return repository.delete(category)

  def all(self) -> List[Category]:
    return repository.all()

  def find(self, id: int) -> Category:
    return repository.find(id)

  def find_by_name(self, name: str) -> Category:
    return repository.find_by_name(name)