from abc import ABC, abstractmethod

class UserFactoryMethod(ABC):
    @abstractmethod
    def create_user(self):
        pass

class DoctorFactoryMethod(UserFactoryMethod):
    def create_user(self):
        return Doctor("U100", "Dr. Bob", "Neurology", "bob@hospital.com")

class AdminFactoryMethod(UserFactoryMethod):
    def create_user(self):
        return AdminStaff("U100", "Alice Admin", "Records", "alice.admin@hospital.com")
