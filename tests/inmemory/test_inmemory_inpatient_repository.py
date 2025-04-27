from repositories.inmemory.inmemory_inpatient_repository import InMemoryInpatientRepository
from models.inpatient import Inpatient

def test_inpatient_crud_operations():
    repo = InMemoryInpatientRepository()
    inpatient = Inpatient(admission_id="a1", patient_id="p1", room_number="101")

    repo.save(inpatient)
    assert repo.find_by_id("a1") == inpatient

    inpatient.room_number = "102"
    repo.save(inpatient)
    assert repo.find_by_id("a1").room_number == "102"

    repo.delete("a1")
    assert repo.find_by_id("a1") is None
