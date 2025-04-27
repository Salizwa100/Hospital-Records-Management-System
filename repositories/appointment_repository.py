from repositories.repository import Repository
from models.appointment import Appointment

class AppointmentRepository(Repository[Appointment, str]):
    pass
