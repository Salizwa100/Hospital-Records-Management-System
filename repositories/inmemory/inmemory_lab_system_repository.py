from repositories.lab_system_repository import LabSystemRepository
from typing import Dict, Optional, List
from models.lab_system import LabSystem

class InMemoryLabSystemRepository(LabSystemRepository):
    def __init__(self):
        self._storage: Dict[str, LabSystem] = {}

    def save(self, entity: LabSystem) -> None:
        self._storage[entity.lab_id] = entity

    def find_by_id(self, id: str) -> Optional[LabSystem]:
        return self._storage.get(id)

    def find_all(self) -> List[LabSystem]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
