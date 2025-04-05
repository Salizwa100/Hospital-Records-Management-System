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

