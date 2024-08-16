from app.models.orden_de_pago import OrdenDePago
from app.repositories.orden_de_pago_repository import OrdenDePagoRepository

class OrdenDePagoService:
    def __init__(self):
        self.orden_de_pago_repository = OrdenDePagoRepository()

    def save(self, orden_de_pago: OrdenDePago) -> OrdenDePago:
        return self.orden_de_pago_repository.save(orden_de_pago)

    def update(self, orden_de_pago: OrdenDePago, id: int) -> OrdenDePago:
        return self.orden_de_pago_repository.update(orden_de_pago, id)

    def delete(self, orden_de_pago: OrdenDePago) -> None:
        self.orden_de_pago_repository.delete(orden_de_pago)

    def all(self) -> List[OrdenDePago]:
        return self.orden_de_pago_repository.all()

    def find(self, id: int) -> OrdenDePago:
        return self.orden_de_pago_repository.find(id)

    def find_by_status(self, status: str) -> List[OrdenDePago]:
        return self.orden_de_pago_repository.find_by_status(status)
