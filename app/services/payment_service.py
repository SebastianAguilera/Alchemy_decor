from typing import List
from app.models import Payment
from app.repositories import PaymentRepository

repository = PaymentRepository()

class PaymentService:
  def save(self, payment: Payment) -> Payment:
    return repository.save(payment)

  def update(self, payment: Payment, id: int) -> Payment:
    return repository.update(payment, id)

  def delete(self, payment: Payment) -> None:
    return repository.delete(payment)

  def all(self) -> List[Payment]:
    return repository.all()

  def find(self, id: int) -> Payment:
    return repository.find(id)

