from repositories.repository import Repository
from models.inpatient import Inpatient

class InpatientRepository(Repository[Inpatient, str]):
    pass 
