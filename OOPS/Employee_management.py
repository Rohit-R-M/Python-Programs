"""
Write a program to build a simple Employee Management System using class Consider 
"""
class Employee:
    def __init__(self,id,name,dept,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_dept=dept
        self.emp_salary=salary
    def display_info(self):
        return f"ID:{self.emp_id}\nName:{self.emp_name}\nDepartment:{self.emp_dept}\nsalary:{self.emp_salary}"
    
class EmployeeManagementSystem:
    def __init__(self):
        self.employees={}

    def add_employee(self,id,name,dept,salary):
        if id in self.employees:
            print("Employee already exist")
        else:
            employee=Employee(id,name,dept,salary)
            self.employees[id]=employee
            print("Employee added successfully")

    def remove_employee(self,id):
        if id not in self.employees:
            print("Employee does not exist")
        else:
            del self.employees[id]
            print("Deleted successfully")

    def disp_employee(self,id):
        if id not in self.employees:
            print("Employee does not exist")
        else:
            print(self.employees[id].display_info())
            
emp=EmployeeManagementSystem()
emp.add_employee(1, "axar", "Networking", 1500000)
emp.add_employee(2, "alice", "cyber", 20000000)
emp.add_employee(3, "john", "Black hat", 12500000)
emp.disp_employee(3)
emp.remove_employee(3)
emp.disp_employee(3)
