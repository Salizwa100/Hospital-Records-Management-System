from repositories.outpatient_repository import OutpatientRepository
from typing import Dict, Optional, List
from models.outpatient import Outpatient

class InMemoryOutpatientRepository(OutpatientRepository):
    def __init__(self):
        self._storage: Dict[str, Outpatient] = {}

    def save(self, entity: Outpatient) -> None:
        self._storage[entity.outpatient_id] = entity

    def find_by_id(self, id: str) -> Optional[Outpatient]:
        return self._storage.get(id)

    def find_all(self) -> List[Outpatient]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
