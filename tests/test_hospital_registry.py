import unittest
from singleton.hospital_registry import HospitalRegistry

class TestHospitalRegistry(unittest.TestCase):
    def test_singleton_instance(self):
        reg1 = HospitalRegistry()
        reg2 = HospitalRegistry()
        self.assertIs(reg1, reg2)

    def test_register_patient(self):
        reg = HospitalRegistry()
        reg.register_patient("P100")
        self.assertIn("P100", reg.get_all_patients())

if __name__ == "__main__":
    unittest.main()
