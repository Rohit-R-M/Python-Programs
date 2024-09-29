"""
Write a program to build a Student Management System using class.
"""
class Student:
    def __init__(self,id,name,age,grade):
        self.student_id=id
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        return f'ID:{self.student_id}\nName:{self.name}\nAge:{self.age}\nGrade:{self.grade}\n'
class StudentManagement:
    def __init__(self):
        self.students={}
    def add_stuent(self,id,name,age,grade):
        if id not in self.students:
            student=Student(id, name, age, grade)
            self.students[id]=student
            print(f'{name} added successfully')
        else:
            print("student already exists")
    def remove_student(self,student_id):
        if student_id not in self.students:
            print("Student not exist")
        else:
            self.students.pop(student_id)
            print("removed student successfully")
    def display_students(self,student_id):
        if student_id not in self.students:
            print("Student not exist")
        else:
            print(self.students[student_id].display_info())
sms=StudentManagement()
sms.add_stuent(1, "sagar", 11, "A") 
sms.add_stuent(2, "anu", 10, "A+")
sms.display_students(1)
sms.remove_student(2)
sms.display_students(2)
