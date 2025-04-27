from repositories.inmemory.inmemory_transfer_repository import InMemoryTransferRepository
from models.transfer import PatientTransfer

def test_transfer_crud_operations():
    repo = InMemoryTransferRepository()
    transfer = PatientTransfer(patient_id="p1", from_department="ER", to_department="ICU")

    repo.save(transfer)
    assert repo.find_by_id("p1") == transfer

    transfer.to_department = "Ward"
    repo.save(transfer)
    assert repo.find_by_id("p1").to_department == "Ward"

    repo.delete("p1")
    assert repo.find_by_id("p1") is None
