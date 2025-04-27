from repositories.repository import Repository
from models.transfer import PatientTransfer

class TransferRepository(Repository[PatientTransfer, str]):
    pass
