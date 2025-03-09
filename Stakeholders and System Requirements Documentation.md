# **1.  Stakeholder Analysis**

| Stakeholders                 | Role                                                       | Key Concerns                                           | Pain Points                                                                                          | Success Metrics |
|------------------------------|------------------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------|
| **1. Patients**                 | <ul><li>Provide personal and health information, receive treatment, book appointments, and expect quality care.</li></ul> | <ul><li>Privacy and security of personal health information.</li><li>Easy accessibility and retrieval of health records (for follow-up visits, second opinions, etc.).</li><li>Ability to pre-book appointments.</li></ul> | <ul><li>Long wait times for file retrievals.</li><li>Difficulty accessing medical history records due to missing files.</li></ul> | <ul><li>Patient satisfaction with easy accessibility to their medical data.</li><li>Reduced waiting time for file retrieval and appointment bookings.</li><li>Receiving quality care as doctors have full medical history records.</li></ul> |
| **2. General Administrators**    | <ul><li>Open files using patient personal details (first-time visits).</li><li>Retrieve files and book appointments (follow-up visits).</li><li>Collect and store patient files after treatment (manual filing process).</li></ul> | <ul><li>Reduce time for opening files for new patients.</li><li>Quick and easy file retrieval of patient files.</li><li>Easy booking of appointments and avoiding overbooking.</li><li>Easy file maintenance (quick and easy updating of patient details, e.g., address and contact details).</li></ul> | <ul><li>No view of appointment bookings (doctors get overbooked).</li><li>File retrieval time is long.</li><li>Files are missing (a new file must be created for the patient).</li><li>Patient details are not updated (not easy to update the details).</li></ul> | <ul><li>System is able to handle hospital capacity and growth (record retrieval is quick).</li><li>70% cost savings through reduced paperwork and improved operational efficiency.</li><li>Track appointment scheduling efficiency, turnaround time, and minimize patient no-show rates.</li><li>The system shall allow 90% of users to perform basic tasks (e.g., displaying and maintaining patient records).</li></ul> |
| **3. Finance Staff**            | <ul><li>Process payments and manage claims.</li></ul>                        | <ul><li>Accurate billing and efficient claim processing.</li></ul> | <ul><li>Incorrect invoices and delays in claim processing.</li></ul> | <ul><li>90% reduction in insurance claims rejections due to accurate data capture (e.g., correct diagnostic/tariff codes).</li><li>Increased billing accuracy.</li></ul> |
| **4. Doctors**                  | <ul><li>Diagnose and treat patients, access medical records.</li></ul>       | <ul><li>Quick access to accurate patient history and integration with lab results.</li></ul> | <ul><li>Manual record retrieval delays and difficulty in tracking medical history.</li></ul> | <ul><li>Retrieve patient records in ≤5 seconds.</li><li>95% accuracy in record updates which leads to increased patient care.</li></ul> |
| **5. Nurses**                   | <ul><li>Administer medication, monitor patient vitals.</li></ul>             | <ul><li>Real-time patient data.</li><li>Detailed log to track medication schedules.</li></ul> | <ul><li>Lack of real-time updates.</li><li>Manual medication tracking errors.</li></ul> | <ul><li>90% adherence to medication schedules.</li><li>Automated patient status updates.</li></ul> |
| **6. IT Staff**                 | <ul><li>Conduct system maintenance, ensure uptime and security.</li></ul>    | <ul><li>System reliability.</li><li>Data security.</li><li>Compliance with HIPAA & GDPR.</li></ul> | <ul><li>Compliance with healthcare standards.</li></ul> | <ul><li>99.9% system uptime.</li><li>Zero security breaches.</li><li>Full compliance with healthcare standards.</li></ul> |
| **7. Pharmacy Administrators**  | <ul><li>Dispatch medication to patients.</li></ul>                           | <ul><li>Accuracy of medication.</li><li>Clear medication substitution.</li></ul> | <ul><li>Not easy to read doctors' handwriting.</li><li>Issuing incorrect medication substitutions.</li></ul> | <ul><li>Ability to stock medication based on trends (e.g., winter patients have flu).</li></ul> |
| **8. Insurance Providers**      | <ul><li>Process claims, verify patient coverage.</li></ul>                  | <ul><li>Fast claim processing.</li><li>Billing accuracy.</li></ul> | <ul><li>Delays in claim approvals.</li><li>Incorrect billing information.</li></ul>  | <ul><li>95% claim processing accuracy.</li><li>40% reduction in reimbursement time.</li></ul> |


# **2.  Functional requirements**

### 2.1.  Patient Management:

1.	The system shall allow registration of new patients with personal details and medical history. 
2.	The system shall allow maintenance of patient records with personal details, diagnosis, prescriptions, and treatments. 
3.	The system shall enable pharmacy administrators to view prescription written by doctors.  
4.	The system shall provide secure access to patient records based on user roles. 
5.	Access shall be roles based (e.g. administrators should have access to only maintain personal details of the patient and have no authorization to display or update medical records of the patient). 
6.	The system shall integrate with lab systems to automatically update test results in patient records. 
7.	The system shall allow doctors to retrieve patient history within 20 seconds.

### 2.2.  Appointment Scheduling:

8.	The system shall enable patients and hospital administrators to book, reschedule, and cancel appointments in real time. 
9.	The system shall ensure that the appointments are only valid once they have been confirmed by hospital administrators. 
10.	The system shall have the automated reminders functionality for patients and doctors.

### 2.3.  Billing and Payments:

11.	The system shall allow billing staff to generate and process invoices digitally for treatments, tests, and prescriptions. 
12.	The system shall show detailed insurance claim processing and payment tracking.

### 2.4.  Reporting and Analytics:

13.	The system shall auto generate statistical reports on hospital operations such as:
  - Outpatients per Department (OPD)
  - 1ST time Visits
  - Follow-ups visits
  - Referrals: Outside vs Internal (general to specialist).
  - Appointments per OPD  
15.	The system shall include a reporting module for the finance department such as: 
  - Billing report. 
  - Invoices report.
  - Patient account report.

### 2.5. Other system functions: 

16.	The system shall maintain a detailed log - a complete audit trail of all data modifications for compliance tracking. 
17.	The system shall enable IT staff to monitor system uptime, logs, and security events.


# **3.  Non-Functional requirements**

### Usability

1.	The system shall have a user-friendly interface with minimal navigation structure complexity to allow users to perform tasks quickly and easy.   
2.	The system shall retrieve records quickly. 
3.	The system shall allow role-based access control to facilitate easier updates and maintenance.
   
## Deployable

4.	The system shall be easily deployable across multiple hospital departments and locations with minimal downtime.
5.	The system shall allow seamless integration with 3rd party systems (e.g. patient portal and lab systems).
   
## Maintainability

6. 	The system shall provide clear error log and monitoring tools to assist IT staff in troubleshooting and system diagnostics.
7. 	The system shall allow seamless updates or patches with minimal disruption to the hospital operations.
   
## Scalability

8. The system shall handle increasing volumes of records, users and new hospital sites without performance degradation. 

## Security
9.	All patient data shall be encrypted to ensure data security and confidentiality of information. 
10.	The system shall implement role-based access control to restrict unauthorized access. 
11.	The system shall comply with healthcare regulations, including HIPAA and GDPR. 
12.	The system shall support audit logging for tracking access and modifications to sensitive data. 
13.	The system shall undergo security vulnerability testing regularly.
    
## Performance
14.	The system response time for any operation shall not exceed 15 seconds to ensure efficiency and effectiveness.
15.	The system shall support high transaction loads without significant performance degradation.





