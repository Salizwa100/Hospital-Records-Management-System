from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository
from models.appointment import Appointment

def test_appointment_crud_operations():
    repo = InMemoryAppointmentRepository()
    appointment = Appointment(appointment_id="app1", patient_id="p1", doctor_id="d1", date="2025-05-01")

    repo.save(appointment)
    assert repo.find_by_id("app1") == appointment

    appointment.date = "2025-05-02"
    repo.save(appointment)
    assert repo.find_by_id("app1").date == "2025-05-02"

    repo.delete("app1")
    assert repo.find_by_id("app1") is None
