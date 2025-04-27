from dataclasses import dataclass

@dataclass
class Patient:
    patient_id: str
    name: str
    age: int
    id_no: str
    gender: str
    contact_number: str
    next_of_keen: str
    address: str
    medical_history: str
