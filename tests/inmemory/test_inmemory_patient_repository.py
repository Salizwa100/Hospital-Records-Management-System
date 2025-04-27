import pytest
from repositories.inmemory.inmemory_patient_repository import InMemoryPatientRepository
from models.patient import Patient

def test_patient_crud_operations():
    repo = InMemoryPatientRepository()
    patient = Patient(patient_id="p1", name="John Doe", age=30)

    # Create
    repo.save(patient)
    assert repo.find_by_id("p1") == patient

    # Read all
    all_patients = repo.find_all()
    assert len(all_patients) == 1

    # Update
    patient.name = "Jane Doe"
    repo.save(patient)
    assert repo.find_by_id("p1").name == "Jane Doe"

    # Delete
    repo.delete("p1")
    assert repo.find_by_id("p1") is None
