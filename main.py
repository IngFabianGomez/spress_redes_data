import json
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

inserted = 0
errors = 0

cur.executescript('''
DROP TABLE IF EXISTS Employee;
CREATE TABLE IF NOT EXISTS Employee (
    Employee_id INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Role TEXT,
    Status TEXT,
    Salary INTEGER
)
''')

FILE_PATH = 'employeesdata.json'

with open (FILE_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

print("")
for emp in data:
    try:
        # Data extraction and cleaning
        emp_id = emp['Employee_id']
        name = (emp.get("Name") or "").strip()
        department = (emp.get("Department") or "").strip()
        role = (emp.get("Role") or "").strip()
        status = (emp.get("Status") or "").strip().capitalize()
        salary = emp['Salary']
        
        # Validate required fields
        required_fields = {
            "Employee_id" : emp_id,
            "Name": name,
            "Department": department,
            "Role": role,
            "Status": status
        }

        # Detect empty required fields
        empty_fields = [
            field for field, value in required_fields.items() if not value
        ]
        
        # Handle empty fields
        if empty_fields:
            print(
                f"Error in record {emp_id}: "
                f"Empty fields → {', '.join(empty_fields)}"
            )
            errors += 1
            continue

        # Validate salary data type
        if not isinstance(salary, int):
            print(f"Error in record {emp_id}: Invalid salary")
            errors += 1
            continue
        
        cur.execute("""
        INSERT INTO Employee (Employee_id, Name, Department, Role, Status, Salary)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (emp_id, name, department, role, status, salary))
        inserted += 1

    except KeyError as e:
        print(f"Missing field {e} in record: {emp}")
        errors += 1

    except sqlite3.IntegrityError:
        print(f"Duplicate employee {emp.get('Employee_id')}")
        errors += 1

conn.commit()

# Final report 
print("\nFINAL REPORT")
print(f"Inserted records: {inserted}")
print(f"Records with errors: {errors}")

# Query active employees 
print("\nACTIVE EMPLOYEES")
for row in cur.execute(
    "SELECT Employee_id, Name, Department, Role FROM Employee WHERE Status = 'Activo'"
):
    print(row)

print("\nINACTIVE EMPLOYEES")
for rows in cur.execute(
    "SELECT Employee_id, Name, Department, Role FROM Employee WHERE Status = 'Inactivo'"
):
    print(rows)
conn.close()