from app.models import ProductColor
from typing import List
from app.repositories import ProductColorRepository

repository = ProductColorRepository()

class ProductColorService:
  def save(self, product_color: ProductColor) -> ProductColor:
    return repository.save(product_color)
  
  def update_stock(self, product_id: int, color_id: int, new_stock: int) -> ProductColor:
    return repository.update_stock(product_id, color_id, new_stock)

  def delete(self, product_id: int, color_id: int) -> None:
    return repository.delete(product_id, color_id)
  
  def find(self, product_id: int, color_id: int) -> ProductColor:
    return repository.find(product_id, color_id)

  def all(self) -> List[ProductColor]:
    return repository.all()