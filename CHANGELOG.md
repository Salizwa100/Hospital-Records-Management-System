# Development Log

## Done

- **Implement LabSystem class**  
  Included in `lab_system.py` with core functionality like `send_results()` and `verify_patient_record_link()`.

- **Implement Bill class and payment methods**  
  Included in `entities.py`, includes `generate_bill`, `submit_claim`, `pay_bill`, and `view_bill`.

- **Implement SystemUser subclasses (AdminStaff, Doctor, Nurse, Patient)**  
  Completed in `users.py`, with method implementations and attributes.

- **Test PatientBuilder, BillPrototype, HospitalRegistry, PatientFactory, UserFactory**  
  Passed all relevant test cases.
##

## Moved to Inprogress

- **Implement User roles**    
  This is currently in developmet, since the System user component has been implemented.
##

## New Issues

- **#18: Improve error handling in LabSystem**  
  Current implementation lacks error checks for edge cases, e.g., verifying if a patient exists before sending results.
  
- **#19: Validate patient-doctor relationship before prescribing or booking appointments**  
  In `Doctor.prescribe_treatment` and `Patient.book_appointments`, there’s no check for valid relationships.

- **#20: Fix broken test in MedicalTeamFactory**  
  `TypeError`: `MedicalTeamFactory.create_doctor()` takes 1 positional argument but 5 were given  
  Update
  

## Unit testing
  

- **#21: Add unit tests for billing operations**  
  Methods in the `Bill` class (e.g., `submit_claim`, `pay_bill`) should be covered by tests to ensure reliability.


