# Reflection - Assignment 9

## 1. Challenges Faced in Designing the Domain Model and Class Diagram

One of the most significant challenges was maintaining the right level of abstraction. In some cases, it was difficult to decide what level of detail should be included in a class. For instance, distinguishing between attributes and relationships for entities like **Bill**, **Prescription**, and **PatientVisit** required several iterations. Initially, it was tempting to overpopulate the **Patient** class with various responsibilities, but the design had to be revised to adhere to the single responsibility principle.

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

