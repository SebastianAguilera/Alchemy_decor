from typing import List, Type
from app.models import User, UserData
from app import db

class UserRepository:

  def save(self, user: User) -> User:
    db.session.add(user)
    db.session.commit()
    return user
  
  def update(self, user: User, id: int) -> User:
    entity = self.find(id)
    if entity is None:
        return None
    entity.username = user.username
    entity.email = user.email
    if user.password is not None:
        entity.password = user.password
    if user.data is not None:
        self.__update_data(entity, user.data)
    db.session.add(entity)
    db.session.commit()
    return entity
  
  def delete(self, user: User) -> None:
    if user.data is not None:
        db.session.delete(user.data)
    db.session.delete(user)
    db.session.commit()

  def all(self) -> List[User]:
    users = db.session.query(User).all()
    return users
  
  def find(self, id: int) -> User:
    if id is None or id == 0:
      return None 
    try:
      return db.session.query(User).filter(User.id == id).one()
    except:
      return None
    
  def find_by_username(self, username: str) -> User: 
    return db.session.query(User).filter(User.username == username).one_or_none()
  
  def find_by_email(self, email: str) -> User:
    return db.session.query(User).filter(User.email.like(f'%{email}%')).all()
  
  def __update_data(self, entity: User, data: UserData):
    entity.data.firstname = data.firstname
    entity.data.lastname = data.lastname
    entity.data.phone = data.phone
    entity.data.address = data.address
    entity.data.city = data.city
    entity.data.country = data.country


