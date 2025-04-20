class UserFactory:
    @staticmethod
    def create_user(user_type):
        if user_type == "doctor":
            return Doctor("S100", "Dr. Alice", "Cardiology", "alice@hospital.com")
        elif user_type == "admin":
            return AdminStaff("S100", "John Admin", "Receptionist", "admin@hospital.com")
        elif user_type == "nurse":
            return Nurse("S100", "Nina Nurse", "Nurse", "nina@hospital.com")
        elif user_type == "patient":
            return Patient("P200", "Peter Patient", date(1990, 12, 15), "Male", "peter1990@gmail.com", "123 Main St", "Anna")
        else:
            raise ValueError("Invalid user type")
