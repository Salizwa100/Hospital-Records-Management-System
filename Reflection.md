#  Reflection - Assignment 6 

### Challenges in Agile Planning
- **Aligning Stakeholder Needs:** Balancing security requirements (user authorizations, compliance) with user experience such as fast access to records was a challenge.
- **Effort Estimation Complexity:** The integrating components such as the insurance provider system and lab systems required cross-team coordination, making estimation tricky.
- **Handling Dependencies:** Some key processes like prescriptions depended on the doctor’s ability to submit them digitally, requiring careful sprint prioritization.
- **Scalability Considerations:** Ensuring that the system implemented can handle growing patient records without affecting speed and reliability required extra planning.

### Lessons Learned
- Stakeholder requirements priorities must be aligned early to avoid conflicts and confusion during the sprint execution.
- Breaking down tasks into smaller portions allows for better sprint flexibility, shared workload, and risk management.
- Testing must be integrated within sprints to ensure processes developed are meeting the stakeholder requirements.
- Automate repetitive processes, such as appointment reminders and lab result updates, to improve efficiency.

#  Reflection - Assignment 7    

### **Challenges in Selecting & Customizing the Template:**

- Choosing a template that is aligned with Agile principles while remaining easy to follow for all team members.   
- Ensuring that the features and columns of the template align with the scope of the project, such as automation and the team size.   
- Customizing the Kanban template to effectively fit task trackers.    

### **GitHub Templates vs Other Tools:**

- **Ease of Use**: GitHub templates are easier to use compared to other tools.
- **Software Development Focus**: GitHub templates are best suited for software development, whereas other tools can accommodate diverse teams beyond developers.
- **3rd Party Integration**: Other tools often support integration with third-party applications.
- **Complex Setup**: Many other tools require a more complex setup process.
- **Code Integration**: Unlike GitHub templates, standalone tools make it challenging for developers to integrate code seamlessly.


# Assignment 8 Reflection

# 1. Choosing Granularity for States/Actions (Balancing Detail vs. Readability)

**Challenge:** The main challenges in modelling state or activity diagrams was deciding how much detail to include too much detail which will lead to unreadable diagram vs too little detail can oversimplify important logic or behaviour.

Example for the Patient Admission workflow, I have struggled with deciding whether to:
- Break down states like "Admitted" into sub-states like "Waiting for Bed Assignment", "Under Initial Evaluation", and "Awaiting Lab Tests", or simply keep a high-level state as "Admitted" for simplicity.    
- In this case I had opted to keeping the high-level state in the state diagram and elaborating sub-activities separately in activity diagrams.    

# 2. Aligning Diagrams with Agile User Stories

**Challenge:** Agile user stories focus on output that the user want's to achieve (e.g., "As a doctor, I want to access a patient's record so that I can review their history"). Translating these into diagrams requires abstraction while staying true to user intent.
Therefore, when it comes to aligning diagrams with evolving user stories can be tricky, especially when stories are split or reprioritized. To overcome this I have decided to label diagrams with user story IDs in oder to	maintain traceability between diagrams and user stories.

# 3. Comparing State Diagrams vs. Activity Diagrams

![image](https://github.com/user-attachments/assets/fdfbeecb-b1c2-4162-a6ed-fce739412923)


# Reflection - Assignment 9

## 1. Challenges Faced in Designing the Domain Model and Class Diagram

One of the most significant challenges was maintaining the right level of abstraction. In some cases, it was difficult to decide what level of detail should be included in a class. For instance, distinguishing between attributes and relationships for entities like **Bill**, **Prescription**, and **PatientVisit** required several iterations. Initially, it was tempting to overpopulate the **Patient** class with various responsibilities, but the design had to be revised to adhere to the *single responsibility principle*.

Modeling relationships also posed challenges, particularly around multiplicities and directionality. For example, accurately capturing that a **Patient** can have multiple **Appointments**, and each **Appointment** must be linked to a **Doctor**, needed careful thought to avoid cyclic dependencies or confusion over ownership. It was also difficult to model bidirectional dependencies without making the diagram overly complex or cluttered.

Defining methods was another area of friction. It was often unclear whether certain behaviours belonged within a particular class or should be handled by a service/controller outside the domain model. For example, deciding whether the **Bill** class should manage `submitClaim()` and `generateBill()` internally or rely on an external billing processor required both design pragmatism and adherence to encapsulation.

---

## 2. Alignment with Previous Assignments

The class diagram aligns closely with earlier assignments, particularly the use case scenarios, state diagrams, and requirements specification. For instance, the **Doctor** class reflects the functional needs defined in the use case for diagnosing patients and prescribing treatment. Similarly, state transitions such as a **Patient** booking an appointment or a **Bill** moving from "unpaid" to "paid" are supported by clearly defined methods and stateful attributes.

The **SystemUser** abstraction, inherited by **Doctor** and **AdminStaff**, reflects role-based access modelled in the system’s security and authentication requirements. Furthermore, the modularity in representing entities like **LabSystem** and **MedicalRecord** aligns with the sequence diagrams and activity flows, where these entities are invoked in a structured and event-driven manner.

---

## 3. Trade-offs Made

Several trade-offs were necessary to balance clarity, extensibility, and complexity. A key trade-off was between **inheritance** and **composition**. In many cases, composition would have offered a more flexible alternative, but inheritance was chosen for simplicity and code reuse, especially for **SystemUser**. However, the design avoided inheriting **Patient** from **SystemUser** to allow future flexibility—such as enabling patient access through a web interface or API without exposing internal system privileges.

Another trade-off was the decision to model some entities, like **Prescription** and **MedicalRecord**, as simplified placeholders rather than full-fledged classes with methods and behaviours. This was done to avoid cluttering the diagram while still signalling their presence in the system’s logic.

---

## 4. Lessons Learned

This exercise served to emphasize a number of crucial lessons concerning object-oriented design:

- **Abstraction** is key to the management of complexity. Achieving the correct scope for every class increases maintainability and communication amongst team members.
- **Encapsulation** improves reliability by ensuring that only relevant operations are allowed on specific objects.
- **Inheritance vs. composition** must be chosen carefully based on the type of relationship. Inheritance must be used for common behaviour, while composition is better for "has-a" relationships.
- **Modelling from requirements** keeps alignment with business goals intact. Traceability from use cases and business rules to the final model keeps the system still relevant to user needs.
- Finally, **visual communication through diagrams** also greatly facilitates understanding and modelling of system behaviour, facilitating collaboration and feedback from stakeholders much easier.



