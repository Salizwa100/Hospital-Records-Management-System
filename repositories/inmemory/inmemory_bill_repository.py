from repositories.bill_repository import BillRepository
from typing import Dict, Optional, List
from models.bill import Bill

class InMemoryBillRepository(BillRepository):
    def __init__(self):
        self._storage: Dict[str, Bill] = {}

    def save(self, entity: Bill) -> None:
        self._storage[entity.bill_id] = entity

    def find_by_id(self, id: str) -> Optional[Bill]:
        return self._storage.get(id)

    def find_all(self) -> List[Bill]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
