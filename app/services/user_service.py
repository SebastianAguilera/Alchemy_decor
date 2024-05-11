from app.models import User
from app.repositories import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_all(self) -> list[User]:
        return self.repository.get_all()

    def get_by_id(self, id)-> User:
        return self.repository.get_by_id(id)

    def create(self, entity: User)-> User:
        return self.repository.create(entity)

    def update(self, id, user) -> User:
        return self.repository.update(id, user)

    def delete(self, id)->bool:
        return self.repository.delete(id)