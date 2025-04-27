from repositories.invoice_repository import InvoiceRepository
from typing import Dict, Optional, List
from models.invoice import Invoice

class InMemoryInvoiceRepository(InvoiceRepository):
    def __init__(self):
        self._storage: Dict[str, Invoice] = {}

    def save(self, entity: Invoice) -> None:
        self._storage[entity.invoice_id] = entity

    def find_by_id(self, id: str) -> Optional[Invoice]:
        return self._storage.get(id)

    def find_all(self) -> List[Invoice]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
