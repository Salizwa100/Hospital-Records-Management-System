import unittest
from abstract_factory.medical_team_factory import MedicalTeamFactory

class TestMedicalTeamFactory(unittest.TestCase):
    def test_create_doctor_and_nurse(self):
        factory = MedicalTeamFactory()
        doctor = factory.create_doctor("U100", "Doc", "Neuro", "999")
        nurse = factory.create_nurse("U101", "Nina", "Nurse", "888")
        self.assertEqual(doctor.specialization, "Neuro")
        self.assertEqual(nurse.name, "Nina")

if __name__ == "__main__":
    unittest.main()
