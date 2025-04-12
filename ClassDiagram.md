```mermaid
classDiagram

%%==================
%% CLASS DEFINITIONS
%%==================

class SystemUser {
  -userId: String
  -username: String
  -password: String
  -role: String
  +login()
  +logout()
  +changePassword()
}

class AdminStaff {
  -staffId: String
  -name: String
  -role: String
  -contactInfo: String
  +createPatientProfile()
  +registerPatientVisit()
  +managePatientRecords()
  +manageAppointments()
}

class Doctor {
  -doctorId: String
  -name: String
  -specialization: String
  -contactInfo: String
  +retrieveMedicalHistory()
  +prescribeTreatment()
  +viewLabResults()
  +diagnosePatient()
}

class Nurse {
  -nurseId: String
  -name: String
  -shiftTime: String
  -contactInfo: String
  +administerMedication()
  +viewPrescriptions()
}

class Patient {
  -patientId: String
  -name: String
  -dateOfBirth: Date
  -gender: String
  -contactInfo: String
  -Address: String
  -nextOfKeen: String
  +bookAppointments()
  +viewMedicalHistory()
  +makePayment()
}

class Bill {
  -billId: String
  -patientId: String
  -doctorId: String
  -dateIssued: Date
  -totalAmount: Float
  -status: String
  -billItems: List
  -insuranceStatus: String
  +generateBill()
  +submitClaim()
  +allocatePayments()
  +viewBill()
}

class LabSystem {
  -labSystemId: String
  -patientId: String
  -doctorId: String
  -resultsStatus: String
  +sendResults()
  +verifyPatientRecordLink()
}

class MedicalRecord
class Appointment
class Prescription
class PatientVisit

%%==================
%% INHERITANCE
%%==================

AdminStaff --|> SystemUser
Doctor --|> SystemUser
Bill --|> SystemUser


%%==================
%% RELATIONSHIPS
%%==================

Patient "1" --> "0..*" Appointment : books
Patient "1" --> "0..*" Bill : associatedWith
Patient "1" --> "1" MedicalRecord : has
Patient "1" --> "0..*" PatientVisit : visits

Doctor "1" --> "0..*" MedicalRecord : creates/updates
Doctor "1" --> "0..*" Appointment : attends
Doctor "1" --> "0..*" Prescription : writes

Nurse "1" --> "0..*" Prescription : reads
Nurse "1" --> "0..*" Patient : assists

AdminStaff "1" --> "0..*" Patient : registers
AdminStaff "1" --> "0..*" Appointment : manages

LabSystem "1" --> "0..*" MedicalRecord : updatesWithResults

Bill "1" --> "0..*" Prescription : includes
Bill "1" --> "1" PatientVisit : for
Bill "1" --> "1" MedicalRecord : linkedTo

%%==================
%% NOTES
%%==================

note for Patient "Only AdminStaff can create Patient profiles.\nPatient can only view their own records.\nValid contact info and next of kin required."
note for Doctor "Can only access records and prescribe for attended patients.\nMust have valid specialization."
note for Nurse "Can view & administer only prescriptions related to their assigned patients.\nCannot diagnose or prescribe."
```


# Key Design Decisions

### 1. Inheritance Structure
- **`SystemUser`** is the base class for login and security features.
- **`Doctor`** and **`AdminStaff`** inherit from `SystemUser` due to their system access needs.
- **`Patient`** was not explicitly inherited to allow optional external access via a different interface.

### 2. Encapsulation of Responsibilities
- Each class contains only attributes and methods relevant to its role.
- For example:
  - **Doctor**: Medical tasks like prescribing and diagnosing.
  - **AdminStaff**: Patient profile creation and appointment handling.
  - **Nurse**: Medication administration based on prescriptions.

### 3. Relationships & Multiplicity
- Real-world constraints influenced the multiplicity:
  - A patient can have many bills and appointments.
  - A doctor can author many prescriptions.
- Multiplicities are explicitly labeled (e.g., `1`, `0..*`) to clarify these associations.

### 4. Composition vs. Association
- **Composition** is used where the relationship is tightly bound (e.g., `Patient` to `MedicalRecord`).
- **Associations** model looser relationships (e.g., `Bill` to `Prescription`).

### 5. Role-Based Access & Security
- System actions are restricted based on roles:
  - Only **doctors** can diagnose.
  - Only **nurses** can administer medication.
  - Only **AdminStaff** can create/edit patient profiles.
- These restrictions are captured through role-specific methods and class separation.

### 6. Modularity and Scalability
- Entities like `LabSystem`, `Prescription`, and `PatientVisit` are modeled as independent classes.
- This promotes modularity and allows easy expansion (e.g., adding pharmacy integration or insurance logic).



