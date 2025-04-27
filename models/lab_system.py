models/lab_system.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LabSystem:
    lab_id: str
    patient_id: str
    doctor_id: str
    lab_results: str
    date_created: datetime

