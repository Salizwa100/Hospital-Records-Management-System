from dataclasses import dataclass
from datetime import datetime

@dataclass
class Inpatient:
    admission_id: str
    patient_id: str
    doctor_name: str
    transfer_type: str
    department: str
    ward: str
    payment_method: str
    date: datetime
