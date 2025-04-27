from dataclasses import dataclass
from datetime import datetime

@dataclass
class Invoice:
    invoice_id: str
    patient_id: str
    doctor_id: str
    treatment_type: str
    amount: float
    status: str
    date_issued: datetime
