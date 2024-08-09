from typing import List
from app.models import Payment
from app import db

class PaymentRepository:

  def save(self, payment: Payment) -> Payment:
    db.session.add(payment)
    db.session.commit()
    return payment

  def update(self, payment: Payment, id: int) -> Payment:
    entity = self.find(id)
    entity.amount = payment.amount
    entity.status = payment.status
    entity.payment_method = payment.payment_method
    entity.payment_date = payment.payment_date
    entity.transaction_id = payment.transaction_id
    db.session.add(entity)
    db.session.commit()
    return entity

  def delete(self, payment: Payment) -> None:
    db.session.delete(payment)
    db.session.commit()

  def all(self) -> List[Payment]:
    payments = db.session.query(Payment).all()
    return payments

  def find(self, id: int) -> Payment:
    if id is None or id == 0:
      return None 
    try:
      return db.session.query(Payment).filter(Payment.id == id).one()
    except:
      return None

  def find_by_name(self, name: str) -> Payment: 
    return db.session.query(Payment).filter(Payment.name == name).one_or_none()