# Similar Assignment Checker  
Software Engineering Project  
Author: Isha Neupane  

---

## Overview  
This project is a "Similar Assignment Checker" designed to compare the content of different student assignments.  
The main purpose is to help detect possible plagiarism by calculating a similarity score between files.

The system was first designed using a UML Class Diagram (StarUML), and the code was later auto-generated and completed in **Python**.

---

##  Project Structure  
Software-engineering-project/
│
├── docs/ # Documentation and UML diagrams
├── src/ # Main source code
│ ├── assignment.py
│ ├── assignmentRepository.py
│ ├── main.py
│ ├── mainApp.py
│ ├── reportGenerator.py
│ ├── similarityEngine.py
│ └── similarityResult.py
│
├── tests/ # (Optional) Test cases
├── README.md
└── submission.md


---

##  Technologies Used  

- Python 3
- StarUML (for UML design)
- VS Code (for development)
- GitHub (version control)

---

##  How the System Works  

### 1. Assignment Repository
Loads multiple assignments from a folder.

### 2. Similarity Engine
Compares assignments by analyzing their text content and produces a similarity score.

### 3. Similarity Result
Stores the results of comparing two assignments.

### 4. Report Generator
Generates a summary or text report for all similarity results.

---

## How to Run the Program  

Step 1 — Clone the repository
git clone https://github.com/IshaNeupane/Software-engineering-project.git

Step 2 — Go to the src folder
cd Software-engineering-project/src

Step 3 — Run the code
python main.py
You will see output like:
Similarity Score: 0.9


## UML Diagram  
The UML Class Diagram for this project is located in:
docs/SystemDesign.uml



It shows the relationships between:  
- Assignment  
- AssignmentRepository  
- SimilarityEngine  
- SimilarityResult  
- ReportGenerator  

---

## 📝 Features  

✔ Load assignments  
✔ Compare content  
✔ Generate similarity score  
✔ UML-driven design  
✔ Clean Python implementation  

---

##  Author  
Isha Neupane  
Southeast Missouri State University  
Software Engineering Project

---

## License  
This project is for academic use only.
