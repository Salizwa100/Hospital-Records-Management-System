class HospitalRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.patients = []
        return cls._instance

    def register_patient(self, patient):
        self.patients.append(patient)

    def list_patients(self):
        for p in self.patients:
            print(f"{p.name} - {p.patient_type()}")
