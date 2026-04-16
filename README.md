<img width="1873" height="999" alt="image" src="https://github.com/user-attachments/assets/81bdbc18-5f77-41ef-b3a9-4f712147884e" />
software-engineer-groupproject
# Study Time Tracker
COMP2116 Software Engineering Group Project

---

## 1. Graphical Abstract
<img width="1873" height="999" alt="image" src="https://github.com/user-attachments/assets/81bdbc18-5f77-41ef-b3a9-4f712147884e" />



---

## 2. Software Purpose

### 2.1 Development Methodology
- **Methodology**: Agile

### 2.2 Reason for Selection
Agile is the optimal methodology for this project, which is centered on personal learning scenarios. Student needs and functional plans will be continuously iterated based on user feedback.

- It supports **phased iterative development**: we can first deliver the core personal time-tracking functions, then gradually roll out extended features, flexibly matching the team's development rhythm.

- Compared with the Waterfall model, Agile can quickly respond to changing requirements. Through continuous testing and optimization, it ensures the software aligns with the actual usage needs of students, reducing development risks.

---

### 2.3 Potential Use Cases / Target Market

#### Core Use Cases
- **For Students**: Track daily study hours, visualize time allocation across different subjects, help students organize their study rhythm, overcome procrastination, and improve self-directed learning efficiency.

#### Target Users
- **Core Users**: Students (primary/secondary school and university) seeking structured personal time management.

---

### Supplementary Note
This software provides a lightweight and practical solution for individual study management. It helps users improve learning efficiency through clear time recording and data visualization.

---

## 3. Development Process

### 3.1 Development Model
- **Model**: Agile + Incremental Development

### Reason for Selection
This project focuses on **local study time management** with clear core functions, which can be gradually expanded based on user feedback.
- Agile supports **short-cycle iteration** and **rapid prototype verification**, making it highly efficient for small-scale projects.
- Compared with the Waterfall model, it is more flexible for UI and function adjustments, ensuring fast delivery of a usable desktop application.

---

### 3.2 Standard Engineering Process
The project strictly follows the standard software development lifecycle:

#### 1. Requirements Analysis
- Collect core requirements for individual student learning scenarios, including study time tracking, subject classification, and note addition.
- Define non-functional requirements such as **data security**, **simple operation**, and **fast response**.
- Establish complete user scenarios from starting timing to data export.

#### 2. System Design
- **Architecture Design**: Use a modular structure, separating the system into UI layer, logic layer, and data persistence layer.
- **Database Design**: Use SQLite for local data storage, with tables such as `study_records` to store subjects, time, and dates.
- **UI Design**: Develop a modern interface using CustomTkinter, including input area, data table, and function operation panel.

#### 3. Implementation
- **UI Development**: Build interactive windows, forms, tables, and buttons using Python and CustomTkinter.
- **Logic Development**: Implement timing functions, input validation, and subject management.
- **Data Layer**: Develop database operations for adding, deleting, querying, and saving records.
- **Visualization**: Use Matplotlib to generate pie charts and bar charts for study data analysis.

#### 4. Unit Testing
- Test timing accuracy and input validation.
- Verify database CRUD operations to ensure stable data storage.
- Validate chart generation and data visualization logic.

#### 5. Integration & Debugging
- Integrate UI, logic, and database modules into a complete system.
- Test full user workflows: add record → view table → generate chart → export CSV.
- Fix bugs related to UI display, data saving, and performance issues.

#### 6. Final Delivery
- Package source code, resources, and `requirements.txt`.
- Complete system verification and deliver a fully functional standalone study time tracker.

---

## 4. Team Roles & Contribution

| Member | Role | Responsibility | Contribution % |
|--------|------|----------------|----------------|
| Member 1 | Project Leader & Core Developer | System development, UI implementation, logic coding, database integration | 34% |
| Member 2 | Requirements & Documentation | Requirement analysis, system design, README documentation, module testing,, project submission,  | 33% |
| Member 3 | Testing & Project Integration | System validation, demo video production,environment configuration | 33% |

---

## 5. Project Timeline
- **Week 1**: Requirement Analysis & System Design
  - Complete requirement gathering, functional specification, and system architecture design
  - Finalize UI layout and database schema for the study time tracker

- **Week 2**: Core Function Development
  - Implement UI interface, timing logic, and database CRUD operations
  - Complete basic record addition, storage, and table display functions

- **Week 3**: Extended Functions & Unit/System Testing
  - Develop data visualization (charts) and CSV export features
  - Conduct unit testing for each module and full system integration testing
  - Fix bugs and optimize system performance and usability

- **Week 4**: Final Integration & Project Submission
  - Package the complete application, update documentation (README)
  - Conduct final acceptance testing and prepare for project submission

---

## 6. Algorithms & Technologies
- Python
- Tkinter / CustomTkinter
- SQLite database
- Matplotlib for charts
- CSV export

---

## 7. Current Status
All functions completed:
- Add study log
- View records
- Delete records
- Generate bar & pie charts
- Export CSV

---

## 8. Future Improvements
- **Global Ranking & School Competition**
  - Implement a school-wide leaderboard that tracks cumulative study hours.
  - Add class/grade group comparison features to foster friendly competition between classes.
  - Display real-time rankings on the homepage to motivate students.
- **User Authentication & School Account System**
  - Add secure login using student ID/school email to ensure only authorized users (students/teachers) can access.
  - Implement teacher/student role separation (admins vs. regular users).
- **Study Group & Community Features**
  - Create class-specific study groups where students can join their grade/class rooms.
  - Add a "Buddy System" to let students find study partners and track each other's progress.
- **Achievement Badges & Rewards**
  - Design badges for milestones (e.g., "100 Hours of Study", "Top of Class").
  - Integrate a reward system to encourage consistent logging across the entire student body.
- **Data Analytics & Reports**
  - Generate school-wide statistics (average study hours, most popular subjects).
  - Provide detailed progress reports for individual students and class teachers.
- **Cloud Sync & Cross-Device Access**
  - Enable cloud sync to allow students to log hours from both desktop and mobile devices.
  - Support for mobile responsive design to ensure usability on phones/tablets.

---

## 9. Demo Video
YouTube URL:https://youtu.be/dAUD9MNTwiE

---

## 10. Development & Runtime Environment
- Language: Python 3.12
- Libraries: customtkinter, tkinter, sqlite3, matplotlib, pandas
- Run command: python main.py

---

## 11. Open Source Declaration
This project uses open-source libraries:
- customtkinter
- tkinter
- matplotlib
- pandas
- sqlite3

All used legally and non-commercially.
