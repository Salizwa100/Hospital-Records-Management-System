from repositories.inmemory.inmemory_outpatient_repository import InMemoryOutpatientRepository
from models.outpatient import Outpatient

def test_outpatient_crud_operations():
    repo = InMemoryOutpatientRepository()
    outpatient = Outpatient(outpatient_id="o1", patient_id="p1", doctor_id="d1")

    repo.save(outpatient)
    assert repo.find_by_id("o1") == outpatient

    outpatient.doctor_id = "d2"
    repo.save(outpatient)
    assert repo.find_by_id("o1").doctor_id == "d2"

    repo.delete("o1")
    assert repo.find_by_id("o1") is None
