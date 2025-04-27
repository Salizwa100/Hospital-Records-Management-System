from repositories.prescription_repository import PrescriptionRepository
from typing import Dict, Optional, List
from models.prescription import Prescription

class InMemoryPrescriptionRepository(PrescriptionRepository):
    def __init__(self):
        self._storage: Dict[str, Prescription] = {}

    def save(self, entity: Prescription) -> None:
        self._storage[entity.prescription_id] = entity

    def find_by_id(self, id: str) -> Optional[Prescription]:
        return self._storage.get(id)

    def find_all(self) -> List[Prescription]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
