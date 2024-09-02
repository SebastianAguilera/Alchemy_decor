from typing import List
from app.models import Role
from app.repositories.role_repository import RoleRepository

class RoleService:
    
    def __init__(self):
        self.repository = RoleRepository()

    def save(self, role: Role) -> Role:
        return self.repository.save(role)

    def update(self, role: Role, id: int) -> Role:
        return self.repository.update(role, id)

    def delete(self, role: Role) -> None:
        return self.repository.delete(role)

    def all(self) -> List[Role]:
        return self.repository.all()

    def find(self, id: int) -> Role:
        return self.repository.find(id)

    def find_by_name(self, name: str) -> Role:
        return self.repository.find_by_name(name)
