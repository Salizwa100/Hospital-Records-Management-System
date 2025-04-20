from simple_factory.system_user import Doctor, Nurse

class MedicalTeamFactory:
    def create_doctor(self, **kwargs):
        return Doctor(**kwargs)

    def create_nurse(self, **kwargs):
        return Nurse(**kwargs)
