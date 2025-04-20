import unittest
from factory_method.user_factory import UserFactory

class TestUserFactory(unittest.TestCase):
    def test_create_doctor(self):
        doctor = UserFactory.create_user("doctor", doctorId="U100", name="Dr. Who", specialization="Cardiology", contactInfo="123")
        self.assertEqual(doctor.name, "Dr. Who")
        self.assertEqual(doctor.role, "Doctor")

if __name__ == "__main__":
    unittest.main()
