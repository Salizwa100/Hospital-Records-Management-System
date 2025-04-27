from dataclasses import dataclass
from datetime import datetime

@dataclass
class Outpatient:
    outpatient_id: str
    patient_id: str
    doctor_name: str
    visit_type: str
    referral_type: str
    department: str
    clinic: str
    payment_method: str
    date: datetime
