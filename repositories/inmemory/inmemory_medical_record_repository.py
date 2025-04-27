from repositories.medical_record_repository import MedicalRecordRepository
from typing import Dict, Optional, List
from models.medical_record import MedicalRecord

class InMemoryMedicalRecordRepository(MedicalRecordRepository):
    def __init__(self):
        self._storage: Dict[str, MedicalRecord] = {}

    def save(self, entity: MedicalRecord) -> None:
        self._storage[entity.record_id] = entity

    def find_by_id(self, id: str) -> Optional[MedicalRecord]:
        return self._storage.get(id)

    def find_all(self) -> List[MedicalRecord]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
