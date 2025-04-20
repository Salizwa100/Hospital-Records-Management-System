from abc import ABC, abstractmethod
from models.staff import Doctor, Nurse

class TreatmentUnitFactory(ABC):
    @abstractmethod
    def assign_doctor(self):
        pass

    @abstractmethod
    def assign_nurse(self):
        pass

class InPatientTreatmentUnitFactory(TreatmentUnitFactory):
    def assign_doctor(self):
        return Doctor()

    def assign_nurse(self):
        return Nurse()

class OutPatientTreatmentUnitFactory(TreatmentUnitFactory):
    def assign_doctor(self):
        return Doctor()

    def assign_nurse(self):
        return Nurse()
