from repositories.inmemory.inmemory_bill_repository import InMemoryBillRepository
from models.bill import Bill

def test_bill_crud_operations():
    repo = InMemoryBillRepository()
    bill = Bill(bill_id="b1", patient_id="p1", total_amount=300.0)

    repo.save(bill)
    assert repo.find_by_id("b1") == bill

    bill.total_amount = 350.0
    repo.save(bill)
    assert repo.find_by_id("b1").total_amount == 350.0

    repo.delete("b1")
    assert repo.find_by_id("b1") is None
