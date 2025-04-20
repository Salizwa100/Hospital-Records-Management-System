from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, name):
        self.name = name
        self.medical_record = []

    def add_to_record(self, entry):
        self.medical_record.append(entry)

    def show_record(self):
        print(f"--- Record for {self.name} ---")
        for entry in self.medical_record:
            print(entry)

    @abstractmethod
    def patient_type(self):
        pass

class InPatient(Patient):
    def patient_type(self):
        return "In-Patient"

class OutPatient(Patient):
    def patient_type(self):
        return "Out-Patient"
