from typing import List
from app.models import Product
from app.repositories import ProductRepository

repository = ProductRepository()

class ProductService:

  def save(self, product: Product) -> Product:
    return repository.save(product)

  def update(self, product: Product, id: int) -> Product:
    return repository.update(product, id)

  def delete(self, product: Product) -> None:
    return repository.delete(product)

  def all(self) -> List[Product]:
    return repository.all()

  def find(self, id: int) -> Product:
    return repository.find(id)

  def find_by_name(self, name: str) -> Product:
    return repository.find_by_name(name)

