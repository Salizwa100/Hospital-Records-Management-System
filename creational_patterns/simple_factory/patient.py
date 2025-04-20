class Patient:
    def __init__(self, patientId, name, dateOfBirth, gender, contactInfo, Address, nextOfKeen):
        self.patientId = patientId
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactInfo = contactInfo
        self.Address = Address
        self.nextOfKeen = nextOfKeen

    def bookAppointments(self):
        return f"{self.name} booked an appointment."

    def viewMedicalHistory(self):
        return f"Viewing medical history for {self.name}."

    def makePayment(self):
        return f"{self.name} made a payment."
