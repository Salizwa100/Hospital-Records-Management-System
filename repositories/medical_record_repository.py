from repositories.repository import Repository
from models.medical_record import MedicalRecord

class MedicalRecordRepository(Repository[MedicalRecord, str]):
    pass
