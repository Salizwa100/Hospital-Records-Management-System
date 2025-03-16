# Use Case Specifications for HRMS

## Key Actors and Their Roles

- **Patient** – Registers in the system, books appointments, retrieves medical history on request, and makes payments. Patients also receive automated reminders for appointments.
- **General Administrator** – Manages patient records, registers patient visits, confirms appointments, and ensures smooth hospital operations by scheduling and updating information.
- **Doctor** – Diagnoses and treats patients, accesses patient history, and reviews lab test results.
- **Nurse** – Administers medication and accesses electronic prescriptions.
- **IT Staff** – Manages system security, enforces MFA, and monitors system logs for security and compliance.
- **Finance Staff** – Processes invoices, handles insurance claims, and ensures accurate billing.
- **Pharmacy Admin** – Views electronic prescriptions and dispenses medication to patients.
- **Insurance Provider** – Verifies patient coverage and approves or rejects insurance claims.
- **Lab System (External)** – Sends lab test results to be linked with patient records.

## Relationships Between Actors and Use Cases

### Generalization

- Both **Patients** and **Administrators** can book, reschedule, or cancel appointments. However, administrators also have the authority to confirm appointments.
- **Doctors** and **Nurses** interact with patient records, but doctors diagnose and prescribe medication, while nurses administer it.

### Inclusion Relationships

- **Book Appointment (UC6)** includes:
  - **Confirmed Appointment (UC8)**
  - **Send Automated Reminders (UC9)**  
  Since every appointment must be confirmed, and reminders are an essential part of the process.

### Extension Relationships

- **Process Insurance Claims (UC11)** extends:
  - **Verify Insurance Coverage (UC21)**  
  Verifying insurance eligibility is a prerequisite for claim processing.

## Addressing Stakeholder Concerns

- **Patients**:  
  The system provides easy appointment booking and secure access to medical records, reducing waiting times and improving access to complete medical history for better treatment.

- **General Administrators**:  
  The system allows quick patient record retrieval to register patient visits and ensures efficient appointment scheduling, avoiding overbooking issues, reducing patient waiting time, and eliminating the physical file retrieval process.

- **Doctors**:  
  By retrieving patient history within 5 seconds, the system ensures accurate diagnoses and smooth integration with lab results, eliminating manual delays and reducing misdiagnosis.

- **Nurses**:  
  They can track medication schedules in real time, reducing errors in medication administration.

- **Finance Staff**:  
  The system ensures accurate billing and reduces insurance claim rejections due to incorrect data.

- **IT Staff**:  
  Ensures compliance with HIPAA & GDPR by enforcing role-based access control and system monitoring.

- **Pharmacy Admins**:  
  Can view digital prescriptions clearly, reducing errors caused by illegible handwriting.

- **Insurance Providers**:  
  Can quickly verify patient coverage, reducing delays in claim approvals.
