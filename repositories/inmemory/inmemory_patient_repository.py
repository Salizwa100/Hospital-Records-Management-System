from repositories.patient_repository import PatientRepository
from typing import Dict, Optional, List
from models.patient import Patient

class InMemoryPatientRepository(PatientRepository):
    def __init__(self):
        self._storage: Dict[str, Patient] = {}

    def save(self, entity: Patient) -> None:
        self._storage[entity.patient_id] = entity

    def find_by_id(self, id: str) -> Optional[Patient]:
        return self._storage.get(id)

    def find_all(self) -> List[Patient]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
