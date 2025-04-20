from abc import ABC, abstractmethod
from models.patient import InPatient, OutPatient

class PatientCreator(ABC):
    @abstractmethod
    def create_patient(self, name):
        pass

class InPatientCreator(PatientCreator):
    def create_patient(self, name):
        return InPatient(name)

class OutPatientCreator(PatientCreator):
    def create_patient(self, name):
        return OutPatient(name)
