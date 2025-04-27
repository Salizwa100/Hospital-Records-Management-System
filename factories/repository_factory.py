from repositories.inmemory.inmemory_patient_repository import InMemoryPatientRepository
from repositories.inmemory.inmemory_outpatient_repository import InMemoryOutpatientRepository
from repositories.inmemory.inmemory_inpatient_repository import InMemoryInpatientRepository
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository
from repositories.inmemory.inmemory_invoice_repository import InMemoryInvoiceRepository
from repositories.inmemory.inmemory_bill_repository import InMemoryBillRepository
from repositories.inmemory.inmemory_prescription_repository import InMemoryPrescriptionRepository
from repositories.inmemory.inmemory_transfer_repository import InMemoryTransferRepository
from repositories.inmemory.inmemory_lab_system_repository import InMemoryLabSystemRepository
from repositories.inmemory.inmemory_medical_record_repository import InMemoryMedicalRecordRepository

from repositories.repository import Repository
from typing import Type, TypeVar
from models.patient import Patient
from models.outpatient import Outpatient
from models.inpatient import Inpatient
from models.appointment import Appointment
from models.invoice import Invoice
from models.bill import Bill
from models.prescription import Prescription
from models.transfer import PatientTransfer
from models.lab_system import LabSystem
from models.medical_record import MedicalRecord

T = TypeVar('T')
ID = TypeVar('ID')

class RepositoryFactory:
    @staticmethod
    def get_repository(entity_class: Type[T]) -> Repository[T, ID]:
        if entity_class == Patient:
            return InMemoryPatientRepository()
        elif entity_class == Outpatient:
            return InMemoryOutpatientRepository()
        elif entity_class == Inpatient:
            return InMemoryInpatientRepository()
        elif entity_class == Appointment:
            return InMemoryAppointmentRepository()
        elif entity_class == Invoice:
            return InMemoryInvoiceRepository()
        elif entity_class == Bill:
            return InMemoryBillRepository()
        elif entity_class == Prescription:
            return InMemoryPrescriptionRepository()
        elif entity_class == PatientTransfer:
            return InMemoryTransferRepository()
        elif entity_class == LabSystem:
            return InMemoryLabSystemRepository()
        elif entity_class == MedicalRecord:
            return InMemoryMedicalRecordRepository()
        else:
            raise ValueError(f"Unsupported entity class: {entity_class}")
