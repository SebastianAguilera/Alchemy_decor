from app.models import Invoice
from typing import List
from app.repositories import InvoiceRepository

class InvoiceService:
    def __init__(self):
        self.invoice_repository = InvoiceRepository()

    def save(self, invoice: Invoice) -> Invoice:
        return self.invoice_repository.save(invoice)

    def update(self, invoice: Invoice, id: int) -> Invoice:
        return self.invoice_repository.update(invoice, id)

    def delete(self, invoice: Invoice) -> None:
        self.invoice_repository.delete(invoice)

    def all(self) -> List[Invoice]:
        return self.invoice_repository.all()

    def find(self, id: int) -> Invoice:
        return self.invoice_repository.find(id)

    def find_by_number(self, number: str) -> Invoice:
        return self.invoice_repository.find_by_number(number)
