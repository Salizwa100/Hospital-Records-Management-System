from repositories.repository import Repository
from models.bill import Bill

class BillRepository(Repository[Bill, str]):
    pass
