from repositories.repository import Repository
from models.invoice import Invoice

class InvoiceRepository(Repository[Invoice, str]):
    pass
