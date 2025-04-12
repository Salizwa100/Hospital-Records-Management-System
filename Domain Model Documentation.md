# 🏥 Domain Model Description

## Entity Descriptions

### 1. Patient

**Attributes**:  
`patientId`, `name`, `dateOfBirth`, `gender`, `contactInfo`, `Address`, `nextOfKeen`

**Methods**:  
- `BookAppointments()`
- `viewMedicalHistory()`
- `makePayment()`

**Relationships**:  
Associated with `MedicalRecord`, `Appointments`, `Billing`

---

### 2.  Doctor

**Attributes**:  
`doctorId`, `name`, `specialization`, `contactInfo`

**Methods**:  
- `retrieveMedicalHistory()`
- `prescribeTreatment()`
- `viewLabResults()`
- `diagnosePatient()`

**Relationships**:  
Attends `Patients`, creates/updates `MedicalRecords`, performs `diagnose` and `Prescriptions`

---

### 3.  Nurse

**Attributes**:  
`nurseId`, `name`, `shiftTime`, `contactInfo`

**Methods**:  
- `administerMedication()`
- `viewPrescriptions()`

**Relationships**:  
Reads `prescriptions`; assists in `treatment`

---

### 4.  Bill

**Attributes**:  
`billId`, `patientID`, `doctorId`, `dateIssued`, `totalAmount`, `status`, `billItems`, `insuranceStatus`

**Methods**:  
- `generateBill()`
- `submitClaim()`
- `allocatePayments()`
- `viewBill()`

**Relationships**:  
Associated with `Patient Prescription`, `PatientVisits`, `MedicalRecord`

---

### 5.  AdminStaff

**Attributes**:  
`staffId`, `name`, `role`, `contactInfo`

**Methods**:  
- `createPatientProfile()`
- `registerPatientVisit()`
- `managePatientRecords()`
- `manageAppointments()`

**Relationships**:  
Can register patient visits, create/edit `Appointments` and `Patient Records`

---

### 6.  LabSystem

**Attributes**:  
`labSystemId`, `patientId`, `doctorId`, `resultsStatus`

**Methods**:  
- `sendResults()`
- `verifyPatientRecordLink()`

**Relationships**:  
Sends test results by attaching them to the patient's `MedicalRecord`

---

### 7.  SystemUser

**Attributes**:  
`userId`, `username`, `password`, `role`

**Methods**:  
- `login()`
- `logout()`
- `changePassword()`

**Relationships**:  
Inherited by `AdminStaff`, `Doctor`, and potentially `Patient`

---

## 📋 Business Rules

### 1.  Patient

- A patient must have a profile created by AdminStaff before booking appointments.
- A patient can only book appointments with available doctors.
- A patient can only view their own medical history.
- A patient can make payments only for bills associated with their visits.
- A patient must have valid contact information and next of kin details to complete registration.

---

### 2.  Doctor

- A doctor can only retrieve the medical history of patients they have attended.
- A doctor can only prescribe treatment for patients with a scheduled appointment.
- A doctor can only view lab results linked to their assigned patients.
- A doctor can only update medical records they created or are authorized to modify.
- A doctor must have a valid specialization to be assigned to a department.

---

### 3.  Nurse

- A Nurse can only administer medications that are listed/prescribed by the Doctor.
- A Nurse must only access/view prescription records related to their assigned shift/patient.
- A Nurse assists in treatments but cannot diagnose or prescribe medication to patients.
- A Nurse can only access the treatment details of patients under their care.

---

### 4.  Bill

- A bill can only be generated for a completed patient visit.
- A bill must include all related medical services and prescriptions.
- A patient can only pay bills associated with their visits.
- A bill's status must be either: `unpaid`, `pending claim`, or `paid`.
- A claim can only be submitted if insurance status is verified.
- Only `FinanceStaff` can generate and manage billing records.

---

### 5.  AdminStaff

- Only AdminStaff can create and update patient profiles.
- AdminStaff can only register a visit if the patient has a valid profile.
- AdminStaff can only manage appointments for registered doctors and patients.
- AdminStaff cannot access or modify prescriptions or medical records created by doctors.

---

### 6.  LabSystem

- LabSystem must verify a valid link between a test result and a patient medical record before sending results.
- Lab results can only be attached to medical records of patients with completed lab orders.
- LabSystem cannot alter diagnosis or treatment plans in the medical record.
- `ResultsStatus` must be updated once results are successfully linked.

---

### 7.  SystemUser

- Only registered users can access the system.
- A SystemUser must log in using a valid username and password.
- Passwords must meet security criteria and be changeable by the user.
- Roles define permissions; e.g., only doctors can prescribe, only nurses can administer medication.
- SystemUser can only perform actions permitted by their assigned role.
