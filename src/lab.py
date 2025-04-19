class LabSystem:
    def __init__(self, lab_system_id: str, patient_id: str, doctor_id: str, results_status: str):
        self.lab_system_id = lab_system_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.results_status = results_status

    def send_results(self):
        print(f"Sending results for patient ID {self.patient_id} to medical record")
        self.results_status = "sent"

    def verify_patient_record_link(self):
        print(f"Verifying link between patient ID {self.patient_id} and medical record")
        return True
