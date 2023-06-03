class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary/50))
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary

        return total_salary
    
    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

    
#Sample data
employee_data = [
    ["E7876", "ADAMS", 50000, "ACCOUNTING"],
    ["E7499", "JONES", 45000, "RESEARCH"],
    ["E7900", "MARTIN", 50000, "SALES"],
    ["E7698", "SMITH", 55000, "OPERATIONS"]
]

# Create Employee objects
employees =[]
for emp_info in employee_data:
    emp = Employee(emp_info[0], emp_info[1], emp_info[2], emp_info[3])
    employees.append(emp)

# Example Usage
emp1 = employees[0]
emp1.assign_department("HR")
emp1.print_employee_details()

emp2 = employees[1]
emp2_salary = emp2.calculate_emp_salary(55)
print("Employee 2 Salary:", emp2_salary)