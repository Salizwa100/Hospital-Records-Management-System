from dataclasses import dataclass

@dataclass
class Prescription:
    prescription_id: str
    patient_id: str
    doctor_id: str
    medication_details: str
