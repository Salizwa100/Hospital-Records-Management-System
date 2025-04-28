import unittest
from src.builder.patient_builder import PatientBuilder

class TestPatientBuilder(unittest.TestCase):
    def test_patient_profile_complete(self):
        builder = PatientBuilder()
        patient = builder.set_basic_info("P200", "Alice", "F", "1985-06-01").set_contact_info("555-1234", "123 Road", "Bob").build()
        self.assertEqual(patient.name, "Alice")
        self.assertEqual(patient.Address, "123 Road")

    def test_missing_fields(self):
        builder = PatientBuilder()
        with self.assertRaises(TypeError):
            builder.build()

if __name__ == "__main__":
    unittest.main()
