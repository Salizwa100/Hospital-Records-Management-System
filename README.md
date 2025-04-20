# Hospital Records Management System  

The purpose of the Hospital Records Management System (HRMS) is to digitize and manage hospital records efficiently. It aims to improve record keeping, patient care, compliance to data security and administrative operations by integrating various hospital departments into a unified digital platform. 

# Links to:

**System Specification Document**   '([SPECIFICATION.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/SPECIFICATION.md))'   

**C4 Architectural Diagrams**  '([ARCHITECTURE.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/ARCHITECTURE.md))'

---

**Assignment 4**    '([Stakeholders and System Requirements Documentation.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Assignment4.md)'     
---
# **Assignment 5**
**Use case Diagrams**  '([Use_Case_Diagram.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Use_Case_Diagram.md))'       


**Use Case Specifications:**  '([Use_Case_Specifications.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Use_Case_Specifications.md))'   

**Test Cases**  '([Test_Cases.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Test_Cases.md))' 

---

# **Assignment 6**

**User Stories**  '([User_Stories.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/User_Stories.md))'        

**Product Backlog**  '([Product_Backlog.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Product_Backlog.md))'      

**Sprint Planning**  '([Sprint_Backlog.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Sprint_Backlog.md))'    

**Reflection**  '([Reflection.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Reflection.md))'       

---

# **Assignment 7**

# **Screenshot**   

### Template comparison
![image](https://github.com/user-attachments/assets/1904437a-69ce-4d10-bd1d-05ffc23c4a96)     

### Custom Kanban board:  

![image](https://github.com/user-attachments/assets/282c8354-cb9b-4dc1-910d-df51dd839a67)     

![image](https://github.com/user-attachments/assets/097e9834-2dbc-4b07-84a7-0b0da570c375)     

## My Kanban Board Customizing choices:

### Added "On hold" Column
To better track tasks that are temporarily paused due to dependencies or other issues, we have introduced an **"On hold"** column. Reason/ Benefits:   
- Visualize blocked items that still require attention.
- Identify dependencies that need resolution.
- Facilitate discussions on tackling blockers during daily standup meetings.

### Added "Testing" Column
To ensure the system meets functional, performance, design, and implementation requirements as outlined in the blueprint and stakeholder requirements list, we have added a **"Testing"** column. Reason/ Benefits:
- Allow verification of system compliance with requirements.
- Help categorize defects or issues for better tracking.
- Enable breaking down logged defects into smaller tasks.
- Assist in assigning issues to the relevant team members for resolution.




### Links:

**Template Analysis and Selection**  '([template_analysis.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/template_analysis.md))'        

**Kanban Board Explanation**  '([kanban_explanation.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/kanban_explanation.md))'

**Reflection**  '([Reflection.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Reflection.md))'  

**Project link** '([Custom Kanban Board Creation](https://github.com/users/Salizwa100/projects/9))'        

---

# **Assignment 8**

**Task 1: Object State Modeling with State Transition Diagrams**  '([State Transition Diagrams with Explainations.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/State%20Transition%20Diagrams%20with%20Explainations.md))'     

**Task 2: Activity Workflow Modeling with Activity Diagrams** '([Activity Workflow with Explainations.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Activity%20Workflow%20with%20Explainations.md))'  


**Reflection**  '([assignment 8_reflection.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/assignment%208_reflection.md))'

---

# **Assignment 9**

**Task 1: Domain Model** '([Domain Model Documentation.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Domain%20Model%20Documentation.md))'

**Task 2: Class Diagram in Mermaid.js** '([Class Diagram.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/ClassDiagram.md))'

**Reflection**  '([Assignment 9 Reflection.md](https://github.com/Salizwa100/Hospital-Records-Management-System/blob/main/Assignment%209%20Reflection.md))'

---
# **Assignment 10**

# **Task 1: Class implementations Source Code** '([Class implementations src folder](https://github.com/Salizwa100/Hospital-Records-Management-System/tree/main/src))'

# Design choice:

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


### 3. `lab_system.py` – Lab Integration
Represents interactions between doctors, patients, and lab results.

- **LabSystem** – Allows linking and sending results securely to medical records.

#### Example:
```python
lab_system.send_results()
```
Updates result status and logs the action.


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


---
**Task 2: Creational patterns Source Code** '([Creational patterns folder](https://github.com/Salizwa100/Hospital-Records-Management-System/tree/main/creational_patterns))'












