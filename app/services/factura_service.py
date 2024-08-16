from app.models.factura import Factura
from app.repositories.factura_repository import FacturaRepository

class FacturaService:
    def __init__(self):
        self.factura_repository = FacturaRepository()

    def save(self, factura: Factura) -> Factura:
        return self.factura_repository.save(factura)

    def update(self, factura: Factura, id: int) -> Factura:
        return self.factura_repository.update(factura, id)

    def delete(self, factura: Factura) -> None:
        self.factura_repository.delete(factura)

    def all(self) -> List[Factura]:
        return self.factura_repository.all()

    def find(self, id: int) -> Factura:
        return self.factura_repository.find(id)

    def find_by_number(self, number: str) -> Factura:
        return self.factura_repository.find_by_number(number)
