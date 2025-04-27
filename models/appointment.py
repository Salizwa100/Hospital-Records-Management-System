from dataclasses import dataclass

@dataclass
class Appointment:
    appointment_id: str
    p_name: str
    patient_id: str
    doctor_id: str
    visit_type: str
    department: str
    clinic: str
    appointment_date: str
    appointment_time: str
