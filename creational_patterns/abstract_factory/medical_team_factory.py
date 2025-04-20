from simple_factory.system_user import Doctor, Nurse

class MedicalTeamFactory:
    def create_doctor(self, user_id: str, name: str, specialization: str, contact_info: str):
        return Doctor(
            user_id=user_id,
            username=name.lower(),
            password="defaultpass",
            role="doctor",
            doctor_id=user_id,
            name=name,
            specialization=specialization,
            contact_info=contact_info
        )

    def create_nurse(self, nurse_id: str, name: str, shift_time: str, contact_info: str):
        return Nurse(
            nurse_id=nurse_id,
            name=name,
            shift_time=shift_time,
            contact_info=contact_info
        )
