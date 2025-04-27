from repositories.inpatient_repository import InpatientRepository
from typing import Dict, Optional, List
from models.inpatient import Inpatient

class InMemoryInpatientRepository(InpatientRepository):
    def __init__(self):
        self._storage: Dict[str, Inpatient] = {}

    def save(self, entity: Inpatient) -> None:
        self._storage[entity.admission_id] = entity

    def find_by_id(self, id: str) -> Optional[Inpatient]:
        return self._storage.get(id)

    def find_all(self) -> List[Inpatient]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
