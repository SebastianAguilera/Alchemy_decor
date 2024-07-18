from app.models import Color
from app.repositories import ColorRepository

class ColorService:
    def __init__(self):
        self.repository = ColorRepository()

    def save(self, color: Color) -> Color:
        return self.repository.save(color)

    def update(self, color: Color, id: int) -> Color:
        return self.repository.update(color, id)

    def delete(self, color: Color) -> None:
        self.repository.delete(color)

    def all(self) -> List[Color]:
        return self.repository.all()

    def find(self, id: int) -> Color:
        return self.repository.find(id)

    def find_by_name(self, name: str) -> Color:
        return self.repository.find_by_name(name)

