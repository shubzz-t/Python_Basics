class Employee:
    _salary=1
    def __init__(self):
        print("CREATED OBJECT")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self , a):
        self._salary=a
        print("SETTER")

emp1=Employee()
emp1.salary=200
print(emp1.salary)

class Programmer(Employee):
    _program=1

    def __init__(self):
        print("PROGRAMMER INITIALIZED")

    def disp(self):
        print(Employee.salary)

pr=Programmer()
pr.disp()