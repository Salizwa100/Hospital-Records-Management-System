import unittest
from factory.patient_factory import PatientCreator

class TestPatientFactory(unittest.TestCase):
    def test_create_patient(self):
        creator = PatientCreator()
        patient = creator.create_patient(patientId="P200", name="John", dateOfBirth="1990-01-01",
                                         gender="M", contactInfo="456", Address="Somewhere", nextOfKeen="Doe")
        self.assertEqual(patient.name, "John")
        self.assertEqual(patient.gender, "M")

if __name__ == "__main__":
    unittest.main()
