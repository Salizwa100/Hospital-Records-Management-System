from models.patient import InPatient, OutPatient
from models.staff import Doctor, Nurse

class PatientRecordBuilder:
    def __init__(self):
        self.patient = None

    def create_patient(self, name, patient_type):
        if patient_type == "in":
            self.patient = InPatient(name)
        else:
            self.patient = OutPatient(name)
        return self

    def doctor_diagnosis(self):
        doc = Doctor()
        doc.diagnose(self.patient)
        return self

    def nurse_treatment(self):
        nurse = Nurse()
        nurse.administer_treatment(self.patient)
        return self

    def build(self):
        return self.patient
