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




