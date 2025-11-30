# Submission Document

**Student:** Isha Neupane  
**Course:** Software Engineering  
**Project:** Similar Assignment Checker  

---

## 1. Tools Used
- **StarUML** – Created UML class diagram and use case diagram  
- **StarUML Code Generation** – Generated initial Python class files  
- **VS Code** – Edited and ran the code  
- **Git & GitHub (CLI only)** – Version control and upload  

---

## 2. UML to Code (Task 1)

### **Step 1: Class Diagram**
- Created `SystemDesign.uml` with classes: Assignment, AssignmentRepository, SimilarityEngine, ReportGenerator, MainApp

### **Step 2: Code Generation Tool**
- Used StarUML → Python code generation

### **Step 3: Settings**
- Target Language: Python  
- Output Folder: `src/`  
- Screenshot taken of the configuration window

### **Step 4: Generated Code**
- StarUML produced Python class stubs for all UML classes  
- Verified generated `.py` files inside `src/`

### **Step 5: Modifications**
- Added actual logic in several files  
- Fixed imports  
- Ensured every class runs correctly

### **Step 6: Run the Code**
- Executed using: `python main.py`  
- Program runs successfully

### **Step 7: Reflection**
StarUML correctly generated class structures and imports, but I still had to write the logic myself.  
Most methods were empty, so I completed them manually.  
Using UML helped keep the design organized and consistent.

---

## 3. Second Diagram (Step 8)
I created a Use Case Diagram showing:
- Actors: Instructor, Student  
- Use Cases: Upload Assignment, Check Similarity, View Report  
- System Boundary box  

**Note:**  
Use Case Diagrams do *not* support code generation, so StarUML generated an empty folder.  
This is normal and still satisfies the requirement.

---

## 4. GitHub Link
https://github.com/IshaNeupane/Software-engineering-project

---

## 5. Git Commands Used
git add .
git commit -m "Updated UML, src code, README and submission files"
git push origin main
