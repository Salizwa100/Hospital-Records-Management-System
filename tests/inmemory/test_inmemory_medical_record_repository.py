from repositories.inmemory.inmemory_medical_record_repository import InMemoryMedicalRecordRepository
from models.medical_record import MedicalRecord

def test_medical_record_crud_operations():
    repo = InMemoryMedicalRecordRepository()
    record = MedicalRecord(record_id="r1", patient_id="p1", diagnosis="Flu")

    repo.save(record)
    assert repo.find_by_id("r1") == record

    record.diagnosis = "Cold"
    repo.save(record)
    assert repo.find_by_id("r1").diagnosis == "Cold"

    repo.delete("r1")
    assert repo.find_by_id("r1") is None
