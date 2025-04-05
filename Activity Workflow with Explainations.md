# UML Activity Workflow Diagrams with Explaination of how the workflow addresses stakeholder concerns

---

## US-001: Patient Registration
```mermaid
flowchart TD
    subgraph PATIENT
        A1([Start]) --> A2[Initiate Registration]
    end

    subgraph SYSTEM
        A2 --> A3[Collect Patient Info]
        A3 --> A4[Validate Input]
        A4 --> B1{Is Input Valid?}
        B1 -- Yes --> A5[Create Patient Profile]
        B1 -- No --> A6[Show Error Message]
    end

    subgraph PATIENT
        A5 --> A7([End])
        A6 --> A7
    end
```

### How it addresses stakeholder concerns:

This workflow addresses patients' concerns about long wait times and difficulty accessing their data. By validating input and creating profiles electronically, it minimizes manual filing errors and reduces delays. Administrators benefit from quicker file creation, helping the hospital scale efficiently.

---

## US-002: Patient Booking Appointments
```mermaid
flowchart TD
    subgraph PATIENT
        B1([Start]) --> B2[Select book/reschedule/cancel]
    end

    subgraph SYSTEM
        B2 --> B3[Check Availability]
        B3 --> B4{Is Time Available?}
        B4 -- Yes --> B5[Confirm or Update Appointment]
        B4 -- No --> B6[Suggest Alternative Slots]
        B5 --> B7[Send Reminder]
        B6 --> B7
    end

    subgraph PATIENT
        B7 --> B8([End])
    end
```
### How it addresses stakeholder concerns: 

Patients can book or modify appointments easily, reducing wait times. Real-time availability checks avoid double-booking—a key concern for both patients and administrators. Automated reminders enhance patient engagement, reducing no-shows and supporting the hospital’s operational efficiency.

---

## US-003: Doctor Views Medical History
```mermaid
flowchart TD
    subgraph DOCTOR
        C1([Start]) --> C2[Request Medical History]
    end

    subgraph SYSTEM
        C2 --> C3[Fetch Patient Data]
        C3 --> C4[Link Lab Results]
        C4 --> C5[Display Data to Doctor]
    end

    subgraph DOCTOR
        C5 --> C6([End])
    end
```
### How it addresses stakeholder concerns:   

Doctors get instant access to accurate patient histories, reducing diagnosis delays. Lab integration ensures up-to-date information, meeting the doctors' need for quick, comprehensive records retrieval within 5 seconds and with 95% accuracy.
   

---

## US-004: Nurse Administers Medication
```mermaid
flowchart TD
    subgraph NURSE
        D1([Start]) --> D2[Select Patient]
    end

    subgraph SYSTEM
        D2 --> D3[Load E-Prescription]
        D3 --> D4[Display Medication Schedule]
    end

    subgraph NURSE
        D4 --> D5[Administer Medication]
    end

    subgraph SYSTEM
        D5 --> D6[Update Medication Record]
    end

    subgraph NURSE
        D6 --> D7([End])
    end
```
### How it addresses stakeholder concerns: 

The workflow ensures that medication schedules are followed accurately. Nurses access and update logs in real time, reducing manual errors and meeting the 90% medication adherence target, a key metric for improving patient care.

---

## US-006: Finance Staff Processes Invoices
```mermaid
flowchart TD
    subgraph FINANCE
        F1([Start]) --> F2[Review Billed Items]
    end

    subgraph SYSTEM
        F2 --> F3[Generate Invoice]
        F3 --> F4[Submit Claim to Insurance]
    end

    subgraph INSURANCE
        F4 --> F5[Verify Patient Coverage]
        F5 --> F6{Is Claim Valid?}
        F6 -- Yes --> F7[Approve & Process Payment]
        F6 -- No --> F8[Flag Issue for Review]
    end

    subgraph FINANCE
        F7 --> F9([End])
        F8 --> F9
    end
```
### How it addresses stakeholder concerns: 

The flow ensures efficient billing and claim submissions, improving billing accuracy and reducing rejections. Automated steps help finance staff meet the 90% claim success target and enhance cash flow reliability.

---

## US-007: Pharmacy Admin Views E-Prescription
```mermaid
flowchart TD
    subgraph PHARMACY_ADMIN
        G1([Start]) --> G2[Search for Patient]
    end

    subgraph SYSTEM
        G2 --> G3[Fetch E-Prescription]
        G3 --> G4[Display Prescription Details]
    end

    subgraph PHARMACY_ADMIN
        G4 --> G5[Dispense Medication]
        G5 --> G6([End])
    end
```
### How it addresses stakeholder concerns: 

Clear digital prescriptions prevent dispensing errors due to illegible handwriting. By integrating e-prescriptions, the system improves accuracy and supports the pharmacist's ability to manage stock based on trends, enhancing service quality.

---

## US-009: Admin Registers Patient & Consultation
```mermaid
flowchart TD
    subgraph ADMIN
        I1([Start]) --> I2[Enter Patient Details]
    end

    subgraph SYSTEM
        I2 --> I3[Check for Existing Record]
        I3 --> I4{Is Patient New?}
        I4 -- Yes --> I5[Create New Record]
        I4 -- No --> I6[Update Existing Record]
        I5 --> I7[Log Consultation]
        I6 --> I7
        I7 --> I8[Update Waiting Queue]
    end

    subgraph ADMIN
        I8 --> I9([End])
    end
```
### How it addresses stakeholder concerns: 

Admins can handle new or returning patients efficiently. This reduces the occurrence of missing files and speeds up waiting room turnover—addressing their pain points around lost records and booking inefficiencies.

---

## US-010: Lab Sends Test Results
```mermaid
flowchart TD
    subgraph LAB_SYSTEM
        J1([Start]) --> J2[Send Test Results]
    end

    subgraph HOSPITAL_SYSTEM
        J2 --> J3[Receive Results]
        J3 --> J4[Match with Patient Record]
        J4 --> J5[Store in Medical History]
        J5 --> J6([End])
    end
```
### How it addresses stakeholder concerns: 

Test results are automatically sent and stored, eliminating delays. Doctors benefit from integrated, timely lab data, enabling faster diagnosis and improving patient outcomes.

---

## US-011: Admin Manages Records
```mermaid
flowchart TD
    subgraph ADMIN
        K1([Start]) --> K2[Search for Patient Record]
    end

    subgraph SYSTEM
        K2 --> K3[Retrieve Record]
    end

    subgraph ADMIN
        K3 --> K4[Update Record if Needed]
        K4 --> K5[Confirm Appointment]
    end

    subgraph SYSTEM
        K5 --> K6[Log Appointment Confirmation]
        K6 --> K7([End])
    end
```
### How it addresses stakeholder concerns: 

Admins can easily search and update records, reducing missing file incidents. This enables quick appointment confirmations and improves administrative efficiency—addressing pain points around slow updates and overbooking.

---

## US-012: IT Staff Manages Roles
```mermaid
flowchart TD
    subgraph IT_STAFF
        L1([Start]) --> L2[Login to System]
        L2 --> L3[Navigate to User Management]
        L3 --> L4[Select Role Operation]
    end

    subgraph SYSTEM
        L4 --> L5[Apply Role Change (Add/Update/Delete)]
        L5 --> L6[Update User Permissions]
        L6 --> L7([End])
    end
```
### How it addresses stakeholder concerns: 
Role-based access ensures security and operational integrity. The workflow aligns with compliance needs and ensures IT staff can maintain and update user roles efficiently with minimal downtime.
