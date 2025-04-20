from abc import ABC, abstractmethod

class MedicalStaff(ABC):
    @abstractmethod
    def role(self):
        pass

class Doctor(MedicalStaff):
    def role(self):
        return "Doctor"

    def diagnose(self, patient):
        patient.add_to_record(f"Diagnosed by Doctor: {patient.name} - Condition: Stable")

class Nurse(MedicalStaff):
    def role(self):
        return "Nurse"

    def administer_treatment(self, patient):
        patient.add_to_record(f"Treatment administered by Nurse: {patient.name} - Medication Given")
