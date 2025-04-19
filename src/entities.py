from datetime import datetime

class Appointment:
    def __init__(self, appointment_id: str, date_time: datetime, status: str, doctor_id: str, patient_id: str):
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.status = status
        self.doctor_id = doctor_id
        self.patient_id = patient_id

class MedicalRecord:
    def __init__(self, record_id: str, diagnosis: str, treatment: str, doctor_id: str, patient_id: str, date_created: datetime):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date_created = date_created

class Bill:
    def __init__(self, bill_id: str, patient_id: str, doctor_id: str, date_issued: datetime, total_amount: float, status: str, bill_items: str, insurance_status: str):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date_issued = date_issued
        self.total_amount = total_amount
        self.status = status
        self.bill_items = bill_items
        self.insurance_status = insurance_status

    def generate_bill(self):
        print(f"Bill {self.bill_id} generated for patient ID {self.patient_id}")

    def submit_claim(self):
        if self.insurance_status.lower() == "verified":
            print(f"Claim submitted for bill ID {self.bill_id}")
        else:
            print("Cannot submit claim: Insurance not verified")

    def pay_bill(self):
        if self.status.lower() != "paid":
            self.status = "paid"
            print(f"Bill {self.bill_id} has been paid.")
        else:
            print(f"Bill {self.bill_id} is already paid.")

    def view_bill(self):
        print(f"Bill ID: {self.bill_id}\nAmount: ${self.total_amount:.2f}\nStatus: {self.status}")
