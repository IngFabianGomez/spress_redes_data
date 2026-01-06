# Employee Management System (Python + JSON + SQLite)

This project is a simple employee management system developed in **Python**, using a **JSON file** as the data source and **SQLite** as the database.  
It simulates a real-world business scenario where employee information must be validated, stored, and queried efficiently.

---

## Features

- Read employee data from a JSON file
- Validate required employee fields
- Detect empty or invalid values
- Prevent duplicate employee records
- Store data in a SQLite database
- Query active and inactive employees
- Generate a final processing report

---

## Technologies Used

- Python 3
- SQLite
- JSON
- Standard Python Libraries (`json`, `sqlite3`, `os`)

---

## Project Structure

employee-management-python/
├── main.py
├── employeesdata.json
├── README.md
├── .gitignore


> The SQLite database (`company.db`) is created automatically when the program runs.

---

## JSON File Format

The application expects a JSON file with the following structure:

```json
[
  {
    "Employee_id": 1001,
    "Name": "John Doe",
    "Department": "Software",
    "Role": "Backend Developer",
    "Status": "ACTIVO",
    "Salary": 4000
  }
]
```

How to Run
Clone the repository:

git clone https://github.com/IngFabianGomez/employee-management-python.git
Run the application:

python main.py

Sample Output
Active employees loaded successfully.
Total employees processed: 5
Active employees found: 3
Inactive employees found: 2

Validation Rules
Required fields must not be empty

Salary must be an integer

Duplicate employee IDs are not allowed

Status values are normalized (ACTIVO / INACTIVO)

Author
Cristhiam Gómez
Mechatronics Engineer | Python | Databases | QA Foundations

LinkedIn: https://www.linkedin.com/in/cristhiam-gomez
GitHub: https://github.com/IngFabianGomez

License

This project is for educational purposes.


