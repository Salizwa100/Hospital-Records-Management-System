from repositories.inmemory.inmemory_lab_system_repository import InMemoryLabSystemRepository
from models.lab_system import LabSystem

def test_lab_system_crud_operations():
    repo = InMemoryLabSystemRepository()
    lab = LabSystem(lab_id="l1", patient_id="p1", test_name="Blood Test")

    repo.save(lab)
    assert repo.find_by_id("l1") == lab

    lab.test_name = "X-Ray"
    repo.save(lab)
    assert repo.find_by_id("l1").test_name == "X-Ray"

    repo.delete("l1")
    assert repo.find_by_id("l1") is None
