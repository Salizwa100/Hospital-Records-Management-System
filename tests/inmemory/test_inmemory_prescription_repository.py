from repositories.inmemory.inmemory_prescription_repository import InMemoryPrescriptionRepository
from models.prescription import Prescription

def test_prescription_crud_operations():
    repo = InMemoryPrescriptionRepository()
    prescription = Prescription(prescription_id="pr1", patient_id="p1", medication="Med1")

    repo.save(prescription)
    assert repo.find_by_id("pr1") == prescription

    prescription.medication = "Med2"
    repo.save(prescription)
    assert repo.find_by_id("pr1").medication == "Med2"

    repo.delete("pr1")
    assert repo.find_by_id("pr1") is None
