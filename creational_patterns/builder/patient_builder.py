from models.patient import Patient

class PatientBuilder:
    def __init__(self):
        self.patient_data = {}

    def set_basic_info(self, patientId, name, gender, dateOfBirth):
        self.patient_data.update({
            "patientId": patientId,
            "name": name,
            "gender": gender,
            "dateOfBirth": dateOfBirth
        })
        return self

    def set_contact_info(self, contactInfo, address, nextOfKeen):
        self.patient_data.update({
            "contactInfo": contactInfo,
            "Address": address,
            "nextOfKeen": nextOfKeen
        })
        return self

    def build(self):
        return Patient(**self.patient_data)
