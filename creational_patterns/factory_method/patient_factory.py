from simple_factory.patient import Patient

class PatientCreator:
    def create_patient(self, **kwargs):
        return Patient(**kwargs)
