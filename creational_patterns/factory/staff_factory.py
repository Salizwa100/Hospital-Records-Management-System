from models.staff import Doctor, Nurse

class StaffFactory:
    @staticmethod
    def create_staff(role):
        if role == "doctor":
            return Doctor()
        elif role == "nurse":
            return Nurse()
        else:
            raise ValueError("Invalid staff role")
