from repositories.repository import Repository
from models.outpatient import Outpatient

class OutpatientRepository(Repository[Outpatient, str]):
    pass
