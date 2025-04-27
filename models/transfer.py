from dataclasses import dataclass
from datetime import datetime

@dataclass
class PatientTransfer:
    patient_id: str
    doctor_id: str
    transfer_from: str
    transfer_to: str
    department: str
    ward: str
    date: datetime
