from repositories.transfer_repository import TransferRepository
from typing import Dict, Optional, List
from models.transfer import PatientTransfer

class InMemoryTransferRepository(TransferRepository):
    def __init__(self):
        self._storage: Dict[str, PatientTransfer] = {}

    def save(self, entity: PatientTransfer) -> None:
        self._storage[entity.patient_id] = entity  # assuming patient_id as key

    def find_by_id(self, id: str) -> Optional[PatientTransfer]:
        return self._storage.get(id)

    def find_all(self) -> List[PatientTransfer]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
