from typing import List#, Type
from app.models import Product
from app import db

class ProductRepository:

  def save(self, product: Product) -> Product:
    db.session.add(product)
    db.session.commit()
    return product

  def update(self, product: Product, id: int) -> Product:
    entity = self.find(id)
    if entity == None:
      return None
    entity.name = product.name
    entity.description = product.description
    entity.price = product.price
    entity.stock = product.stock
    db.session.add(entity)
    db.session.commit()
    return entity

  def delete(self, product: Product) -> None:
    db.session.delete(product)
    db.session.commit()

  def all(self) -> List[Product]:
    products = db.session.query(Product).all()
    return products

  def find(self, id: int) -> Product:
    if id is None or id == 0:
      return None 
    try:
      return db.session.query(Product).filter(Product.id == id).one()
    except:
      return None

  def find_by_name(self, name: str) -> Product: 
    return db.session.query(Product).filter(Product.name == name).one_or_none()
