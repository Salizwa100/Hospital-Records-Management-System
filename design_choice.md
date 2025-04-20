
# 🏥 Hospital Records Management System – Design choice

## 📌 Why Python?

Python was chosen for this project due to its:

- **Simplicity and readability** – great for collaboration and maintenance.
- **Rich libraries** – such as `datetime` for handling time-based data.
- **Object-oriented design** – perfect for modeling real-world entities like doctors, patients, and appointments.
- **Rapid prototyping** – allows for faster development cycles with fewer lines of code.

## Overview of Modules

This system is composed of three main Python files:

### 1. `users.py` – User Roles and Permissions
Defines core users and their specific responsibilities:

- **SystemUser** – A base class with login, logout, and password management features.
- **Doctor, Nurse, AdminStaff, Patient** – Inherit from `SystemUser` or standalone, each with domain-specific methods.

#### Example:
```python
doctor.prescribe_treatment("patient123", "Paracetamol 500mg")
```
This lets a doctor issue a prescription for a patient.

---

### 2. `entities.py` – Core Data Models
Encapsulates entities such as:

- **Appointment** – Handles scheduling between doctors and patients.
- **MedicalRecord** – Stores diagnosis, treatment, and date of entry.
- **Bill** – Tracks billing details with methods for payment, claim submission, and viewing.

#### Example:
```python
bill.pay_bill()
```
Changes bill status and confirms payment.

---

### 3. `lab_system.py` – Lab Integration
Represents interactions between doctors, patients, and lab results.

- **LabSystem** – Allows linking and sending results securely to medical records.

#### Example:
```python
lab_system.send_results()
```
Updates result status and logs the action.

---

## Key Design Decisions

### ✅ Object-Oriented Design
Every major component (like users, bills, appointments) is modeled as a class to mirror real-world entities.

### ✅ Inheritance
Shared functionality (like authentication) is implemented in a base `SystemUser` class and extended in specialized roles like `Doctor` and `Patient`.

### ✅ Encapsulation
User details and operations (e.g., passwords) are kept private (`_password`) to protect data integrity.

### ✅ Simple Role-Based Methods
Each class includes intuitive methods specific to the role:
- `Doctor.diagnose_patient()`
- `AdminStaff.register_patient_visit()`
- `Patient.make_payment()`
