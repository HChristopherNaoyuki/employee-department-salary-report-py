# Employee Salary Report

## Overview

This Python program calculates and displays a report of employee salaries categorized by department. The report includes the total and average salary for each department, and lists employees along with their salaries. The program uses parallel arrays to store employee names, department numbers, and salaries.

## Functionality

1. **Employee Class**:

   * The `Employee` class is responsible for storing and processing employee data.
   * The class contains the following arrays:

     * `EmployeeNames`: A list of employee names.
     * `Departments`: A list of department IDs corresponding to each employee.
     * `Salaries`: A list of employee salaries.
     * `DepartmentTotal`: A list that stores the total salary of each department.
     * `DepartmentCount`: A list that stores the count of employees in each department.
     * `DepartmentAverage`: A list that stores the average salary of each department.

2. **Data Initialization**:

   * The program populates the `EmployeeNames`, `Departments`, and `Salaries` arrays with sample data.

3. **Salary Calculation**:

   * The total salary and count of employees in each department are calculated.
   * The average salary for each department is then calculated by dividing the department's total salary by the number of employees in that department.

4. **Report Generation**:

   * A detailed report is printed, showing each employee's name, salary, and department.
   * The average salary of each department is displayed at the end of each department's list of employees.

## Code Walkthrough

### 1. `Employee` Class Definition

```python
class Employee:
    def __init__(self):
        # Initialize arrays for employee data
        self.EmployeeNames = [""] * 5
        self.Departments = [0] * 5
        self.Salaries = [0] * 5
        self.DepartmentTotal = [0] * 3
        self.DepartmentCount = [0] * 3
        self.DepartmentAverage = [0] * 3
```

* In the constructor (`__init__`), arrays for employee names, departments, salaries, department totals, department counts, and department averages are initialized.

### 2. `process_data` Method

```python
def process_data(self):
    # Initialize employee data
    self.EmployeeNames[0] = "Bongi"
    self.EmployeeNames[1] = "Tyrone"
    self.EmployeeNames[2] = "Priya"
    self.EmployeeNames[3] = "Joseph"
    self.EmployeeNames[4] = "Jason"

    self.Departments[0] = 1
    self.Departments[1] = 1
    self.Departments[2] = 2
    self.Departments[3] = 2
    self.Departments[4] = 3

    self.Salaries[0] = 33000
    self.Salaries[1] = 25000
    self.Salaries[2] = 85000
    self.Salaries[3] = 12000
    self.Salaries[4] = 50000

    # Calculate department totals and counts
    i = 0
    while i < 5:
        self.DepartmentTotal[self.Departments[i] - 1] += self.Salaries[i]
        self.DepartmentCount[self.Departments[i] - 1] += 1
        i += 1

    # Calculate department averages
    j = 0
    while j < 3:
        if self.DepartmentCount[j] != 0:
            self.DepartmentAverage[j] = self.DepartmentTotal[j] // self.DepartmentCount[j]
        else:
            self.DepartmentAverage[j] = 0
        j += 1
```

* Data for 5 employees, including their names, departments, and salaries, is initialized.
* The method then calculates the total salary for each department and counts how many employees belong to each department.
* After that, the average salary for each department is calculated using integer division.

### 3. Report Display

```python
    # Display the report 
    print("********************************************************************")
    print("DEPARTMENT\tEMPLOYEE\tSALARY (R)\t\tAVERAGE (R)")
    print("********************************************************************")

    k = 0
    while k < 5:
        if k == 0 or self.Departments[k] != self.Departments[k - 1]:
            print(f"{self.Departments[k]}\t\t{self.EmployeeNames[k]}\t\t{self.Salaries[k]}")
        else:
            print(f"\t\t{self.EmployeeNames[k]}\t\t{self.Salaries[k]}")

        k += 1
        # Display average if it's the last employee in the department
        if k == 5 or self.Departments[k] != self.Departments[k - 1]:
            print(f"\t\t\t\t\t\t\t{self.DepartmentAverage[self.Departments[k - 1] - 1]}")

    print("********************************************************************")
```

* The program prints the header of the report and then iterates through the employees to display their names, salaries, and departments.
* After listing the employees for each department, the average salary for that department is printed.

### 4. Running the Report

```python
# Create instance and run the report
emp = Employee()
emp.process_data()
```

* An instance of the `Employee` class is created and the `process_data()` method is called to generate the report.

## Example Output

```text
********************************************************************
DEPARTMENT    EMPLOYEE        SALARY (R)        AVERAGE (R)
********************************************************************
1            Bongi           33000
             Tyrone          25000
                                                  29000
2            Priya           85000
             Joseph          12000
                                                  48500
3            Jason           50000
                                                  50000
********************************************************************
```

## Notes

* The program currently works with hardcoded employee data. You can modify the data in the `process_data()` method as needed.
* The department IDs range from 1 to 3, and the average salaries are calculated accordingly.

## Future Enhancements

* Allow the user to input employee data dynamically (e.g., via a form or command-line input).
* Handle cases where employees might belong to more than three departments.
* Add error checking for invalid data (e.g., negative salaries or invalid department IDs).

## License

This code is released under the MIT License. Feel free to modify and use it for your projects.
