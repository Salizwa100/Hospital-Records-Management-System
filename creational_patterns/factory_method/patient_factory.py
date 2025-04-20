from models.patient import Patient

class PatientCreator:
    def create_patient(self, **kwargs):
        return Patient(**kwargs)
