# Start 

class Employee:
    # Declare and initialize parallel arrays 
    def __init__(self):
        # Declarations 
        self.EmployeeNames = [""] * 5
        self.Departments = [0] * 5
        self.Salaries = [0] * 5
        self.DepartmentTotal = [0] * 3
        self.DepartmentCount = [0] * 3
        self.DepartmentAverage = [0] * 3

    def process_data(self):
        # Initialize arrays with given data 
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

        # Calculate total salary and count for each department 
        i = 0
        while i < 5:
            self.DepartmentTotal[self.Departments[i] - 1] += self.Salaries[i]
            self.DepartmentCount[self.Departments[i] - 1] += 1
            i = i + 1

        # Calculate average salary per department 
        j = 0
        while j < 3:
            if self.DepartmentCount[j] != 0:
                # Outcomes: 
                # Under department 1: 29000 
                # Under department 2: 48500 
                # Under department 3: 50000 
                self.DepartmentAverage[j] = self.DepartmentTotal[j] // self.DepartmentCount[j]
            else:
                self.DepartmentAverage[j] = 0 # Prevent division by zero error 
            j = j + 1

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
            
            k = k + 1
            # Display average if it's the last employee in the department 
            if k == 5 or self.Departments[k] != self.Departments[k - 1]:
                print(f"\t\t\t\t\t\t\t{self.DepartmentAverage[self.Departments[k - 1] - 1]}")

        print("********************************************************************")

# Create instance and run the report
emp = Employee()
emp.process_data()

# Stop 