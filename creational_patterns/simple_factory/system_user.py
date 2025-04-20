class SystemUser:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    def login(self):
        return f"{self.username} logged in."

    def logout(self):
        return f"{self.username} logged out."

    def changePassword(self, new_password):
        self.password = new_password
        return "Password changed successfully."


class AdminStaff(SystemUser):
    def __init__(self, staffId, name, role, contactInfo):
        super().__init__(staffId, name, "admin123", "AdminStaff")
        self.staffId = staffId
        self.name = name
        self.contactInfo = contactInfo

    def createPatientProfile(self, patient):
        return f"Patient profile for {patient.name} created by {self.name}."

    def registerPatientVisit(self, patient):
        return f"Patient {patient.name} visit registered."

    def managePatientRecords(self):
        return "Managing patient records."

    def manageAppointments(self):
        return "Managing appointments."


class Doctor(SystemUser):
    def __init__(self, doctorId, name, specialization, contactInfo):
        super().__init__(doctorId, name, "doc123", "Doctor")
        self.doctorId = doctorId
        self.name = name
        self.specialization = specialization
        self.contactInfo = contactInfo

    def retrieveMedicalHistory(self, patient):
        return f"Medical history retrieved for patient {patient.name}."

    def prescribeTreatment(self, patient, treatment):
        return f"Prescribed '{treatment}' to {patient.name}."

    def viewLabResults(self, patient):
        return f"Lab results viewed for {patient.name}."

    def diagnosePatient(self, patient):
        return f"Diagnosed patient {patient.name}."


class Nurse(SystemUser):
    def __init__(self, nurseId, name, shiftTime, contactInfo):
        super().__init__(nurseId, name, "nurse123", "Nurse")
        self.nurseId = nurseId
        self.name = name
        self.shiftTime = shiftTime
        self.contactInfo = contactInfo

    def administerMedication(self, patient, medication):
        return f"{self.name} administered {medication} to {patient.name}."

    def viewPrescriptions(self, patient):
        return f"Viewing prescriptions for {patient.name}."
