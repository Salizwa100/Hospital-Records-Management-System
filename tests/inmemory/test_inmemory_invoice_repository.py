from repositories.inmemory.inmemory_invoice_repository import InMemoryInvoiceRepository
from models.invoice import Invoice

def test_invoice_crud_operations():
    repo = InMemoryInvoiceRepository()
    invoice = Invoice(invoice_id="inv1", patient_id="p1", amount=200.0)

    repo.save(invoice)
    assert repo.find_by_id("inv1") == invoice

    invoice.amount = 250.0
    repo.save(invoice)
    assert repo.find_by_id("inv1").amount == 250.0

    repo.delete("inv1")
    assert repo.find_by_id("inv1") is None
