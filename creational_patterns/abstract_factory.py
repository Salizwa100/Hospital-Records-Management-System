from abc import ABC, abstractmethod
from datetime import date

# === Product Interfaces ===

class SystemUser(ABC):
    def __init__(self, user_id, name, contact_info):
        self.user_id = user_id
        self.name = name
        self.contact_info = contact_info

    @abstractmethod
    def get_role(self):
        pass


# === Concrete Products ===

class Doctor(SystemUser):
    def __init__(self, user_id, name, specialization, contact_info):
        super().__init__(user_id, name, contact_info)
        self.specialization = specialization

    def get_role(self):
        return "Doctor"

    def diagnose_patient(self):
        print(f"{self.name} is diagnosing the patient.")

    def prescribe_treatment(self):
        print(f"{self.name} prescribed treatment.")

class AdminStaff(SystemUser):
    def __init__(self, user_id, name, role, contact_info):
        super().__init__(user_id, name, contact_info)
        self.role = role

    def get_role(self):
        return "AdminStaff"

    def create_patient_profile(self):
        print(f"{self.name} is creating a patient profile.")

class Nurse(SystemUser):
    def __init__(self, user_id, name, shift_time, contact_info):
        super().__init__(user_id, name, contact_info)
        self.shift_time = shift_time

    def get_role(self):
        return "Nurse"

    def administer_medication(self):
        print(f"{self.name} is administering medication.")

class Patient:
    def __init__(self, patient_id, name, dob, gender, contact_info, address, next_of_kin):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = dob
        self.gender = gender
        self.contact_info = contact_info
        self.address = address
        self.next_of_kin = next_of_kin

    def get_role(self):
        return "Patient"

    def book_appointments(self):
        print(f"{self.name} is booking an appointment.")


# === Abstract Factory ===

class UserFactory(ABC):
    @abstractmethod
    def create_user(self):
        pass


# === Concrete Factories ===

class DoctorFactory(UserFactory):
    def create_user(self):
        return Doctor(
            user_id="U100",
            name="Dr. Alice",
            specialization="Cardiology",
            contact_info="alice@hospital.com"
        )

class AdminStaffFactory(UserFactory):
    def create_user(self):
        return AdminStaff(
            user_id="U101",
            name="John Admin",
            role="Receptionist",
            contact_info="john.admin@hospital.com"
        )

class NurseFactory(UserFactory):
    def create_user(self):
        return Nurse(
            user_id="U103",
            name="Nina Nurse",
            shift_time="Nurse",
            contact_info="nina@hospital.com"
        )

class PatientFactory(UserFactory):
    def create_user(self):
        return Patient(
            patient_id="P200",
            name="Peter Patient",
            dob=date(1991, 10, 15),
            gender="Male",
            contact_info="peter1991@gmail.com",
            address="123 Main St",
            next_of_kin="Anna Land"
        )


# === Client Code ===

def create_and_show_user(factory: UserFactory):
    user = factory.create_user()
    print(f"Created: {user.get_role()} - {user.name}")
    return user


if __name__ == "__main__":
    doctor = create_and_show_user(DoctorFactory())
    admin = create_and_show_user(AdminStaffFactory())
    nurse = create_and_show_user(NurseFactory())
    patient = create_and_show_user(PatientFactory())
