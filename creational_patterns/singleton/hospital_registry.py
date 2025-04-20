class HospitalRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HospitalRegistry, cls).__new__(cls)
            cls._instance.patients = []
            cls._instance.staff = []
        return cls._instance

    def register_patient(self, patient):
        self.patients.append(patient)

    def register_staff(self, user):
        self.staff.append(user)

    def get_all_patients(self):
        return self.patients

    def get_all_staff(self):
        return self.staff
