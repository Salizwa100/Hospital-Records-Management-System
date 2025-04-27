from repositories.repository import Repository
from models.patient import Patient

class PatientRepository(Repository[Patient, str]):
    pass
