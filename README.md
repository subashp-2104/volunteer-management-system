# Volunteer Management System

## Overview

The **Volunteer Management System** is a Python-based application developed to manage volunteer information efficiently.

This project provides a simple menu-driven interface that allows users to register new volunteers, view volunteer records, search for volunteers by name, filter volunteers based on their skills, and generate reports.

All volunteer information is stored in a CSV file using Python's CSV file handling functionality, making data storage and retrieval simple and efficient.

## Features

- **Volunteer Registration** – Register new volunteers by entering their personal and contact details.
- **View Volunteers** – Display all registered volunteer records.
- **Search Volunteer** – Search for volunteers using their names.
- **Filter By Skill** – Find volunteers based on specific skills.
- **Generate Report** – Display the total number of registered volunteers.
- **CSV-Based Data Storage** – Store and retrieve volunteer information using CSV files.
- **Menu-Driven Interface** – Simple and user-friendly command-line interaction.

## Technologies Used

- Python
- CSV Module
- File Handling
- Functions
- Loops and Conditional Statements
- Command-Line Interface (CLI)

## Project Structure

```text
Volunteer Management System/
│
├── main.py
├── volunteers.csv
├── requirements.txt
├── Output.png
└── README.md
```

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Volunteer-Management-System.git
```

### Step 2: Navigate to the Project Folder

```bash
cd "Volunteer Management System"
```

### Step 3: Run the Application

```bash
python main.py
```

**Note:** Python 3 must be installed on your system. No external packages are required because the project uses Python's built-in CSV module.

## Available Functions

### 1. Add Volunteer

Allows users to register new volunteers by collecting the following details:

- Name
- Age
- Phone Number
- Email Address
- Skill

The entered information is stored in the CSV file.

### 2. View Volunteers

Displays all volunteer records stored in the CSV file.

### 3. Search Volunteer

Allows users to search for registered volunteers using their names.

### 4. Filter By Skill

Filters volunteer records based on specific skills.

**Example Skills:**
- Teaching
- Fundraising
- Event Management
- Social Media

Users can enter a skill to find volunteers with matching skills.

### 5. Generate Report

Generates a simple report by counting the total number of registered volunteers.

**Sample Report:**

```text
===== REPORT =====

Total Volunteers: 10
```

### 6. Exit

Terminates the application safely.

## Sample Output

```text
====== VOLUNTEER MANAGEMENT SYSTEM ======

1. Add Volunteer
2. View Volunteers
3. Search Volunteer
4. Filter By Skill
5. Generate Report
6. Exit

Enter Choice: 1

Enter Name: Subash
Enter Age: 21
Enter Phone: 9876543210
Enter Email: subash@gmail.com
Enter Skill: Teaching

Volunteer Registered Successfully!
```

## Output Screenshot

![Volunteer Management System Output](Output.png)

## Applications

- NGO Volunteer Management
- Community Service Programs
- Social Welfare Organizations
- Event Coordination
- Educational Institutions
- Volunteer Registration Systems

## Future Enhancements

- Graphical User Interface (GUI)
- SQLite Database Integration
- Volunteer Attendance Tracking
- Email Notifications
- PDF Report Generation
- Admin Login and Authentication
- Advanced Volunteer Search and Filtering

## Author

**SUBASH P**

B.E. Computer Science and Engineering (AI & ML)

## GitHub Topics

```text
python
volunteer-management
csv-storage
file-handling
python-project
beginner-project
social-impact
```

---

⭐ If you find this project useful, consider giving it a star on GitHub!
