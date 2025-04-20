from simple_factory.system_user import Doctor, Nurse, AdminStaff

class UserFactory:
    @staticmethod
    def create_user(role, **kwargs):
        if role == "doctor":
            return Doctor(**kwargs)
        elif role == "nurse":
            return Nurse(**kwargs)
        elif role == "admin":
            return AdminStaff(**kwargs)
        else:
            raise ValueError("Invalid user role")
