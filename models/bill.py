from dataclasses import dataclass
from datetime import datetime

@dataclass
class Bill:
    bill_id: str
    patient_id: str
    doctor_id: str
    date_issued: datetime
    total_amount: float
    status: str
    bill_items: str
    insurance_status: str
