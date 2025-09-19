# Modified version - Employee and Company classes
class Employee:
    def __init__(self, name, emp_id, skills=None):
        self.employee_name = name
        self.employee_id = emp_id
        self.skills = skills if skills is not None else []

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_info(self):
        return f"Employee: {self.employee_name}, ID: {self.employee_id}, Skills: {', '.join(self.skills)}"

class Company:
    def __init__(self, company_name, employees=None):
        self.name = company_name
        self.employees = employees if employees is not None else []

    def hire_employee(self, employee):
        self.employees.append(employee)

    def company_info(self):
        return f"Company: {self.name}, Total Employees: {len(self.employees)}"

# Example usage
emp1 = Employee("John", 201, ["Python", "Java"])
comp1 = Company("Tech Solutions")
comp1.hire_employee(emp1)
print(emp1.get_info())
print(comp1.company_info())
