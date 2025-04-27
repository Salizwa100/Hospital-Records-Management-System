from repositories.repository import Repository
from models.prescription import Prescription

class PrescriptionRepository(Repository[Prescription, str]):
    pass
