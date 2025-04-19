from datetime import datetime

class SystemUser:
    def __init__(self, user_id: str, username: str, password: str, role: str):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._role = role

    def login(self):
        print(f"{self._username} logged in.")

    def logout(self):
        print(f"{self._username} logged out.")

    def change_password(self, new_password: str):
        self._password = new_password
        print("Password changed successfully.")

class AdminStaff(SystemUser):
    def __init__(self, user_id, username, password, role, staff_id, name, contact_info):
        super().__init__(user_id, username, password, role)
        self.staff_id = staff_id
        self.name = name
        self.contact_info = contact_info

    def create_patient_profile(self, patient):
        print(f"Created profile for patient: {patient.name}")

    def register_patient_visit(self, patient_id: str):
        print(f"Registered visit for patient ID: {patient_id}")

    def manage_patient_records(self):
        print("Managing patient records...")

    def manage_appointments(self):
        print("Managing appointments...")

class Doctor(SystemUser):
    def __init__(self, user_id, username, password, role, doctor_id, name, specialization, contact_info):
        super().__init__(user_id, username, password, role)
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact_info = contact_info

    def retrieve_medical_history(self, patient_id: str):
        print(f"Retrieving medical history for patient ID: {patient_id}")

    def prescribe_treatment(self, patient_id: str, treatment: str):
        print(f"Prescribed '{treatment}' to patient ID: {patient_id}")

    def view_lab_results(self, patient_id: str):
        print(f"Viewing lab results for patient ID: {patient_id}")

    def diagnose_patient(self, patient_id: str, diagnosis: str):
        print(f"Diagnosed patient ID {patient_id} with: {diagnosis}")

class Nurse:
    def __init__(self, nurse_id: str, name: str, shift_time: str, contact_info: str):
        self.nurse_id = nurse_id
        self.name = name
        self.shift_time = shift_time
        self.contact_info = contact_info

    def administer_medication(self, patient_id: str, medication: str):
        print(f"Administered '{medication}' to patient ID: {patient_id}")

    def view_prescriptions(self, patient_id: str):
        print(f"Viewing prescriptions for patient ID: {patient_id}")

class Patient(SystemUser):
    def __init__(self, user_id, username, password, role, patient_id, name, date_of_birth, gender, contact_info, address, next_of_kin):
        super().__init__(user_id, username, password, role)
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_info = contact_info
        self.address = address
        self.next_of_kin = next_of_kin

    def book_appointments(self, doctor_id: str, date_time: datetime):
        print(f"Appointment booked with doctor ID {doctor_id} at {date_time}")

    def view_medical_history(self):
        print(f"Viewing medical history for patient: {self.name}")

    def make_payment(self, amount: float):
        print(f"Payment of ${amount:.2f} made by patient: {self.name}")
