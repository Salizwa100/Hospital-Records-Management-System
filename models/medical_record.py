from dataclasses import dataclass
from datetime import datetime

@dataclass
class MedicalRecord:
    record_id: str
    patient_id: str
    doctor_id: str
    lab_results: str
    diagnosis: str
    treatment: str
    date_created: datetime
