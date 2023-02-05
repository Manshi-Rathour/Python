class Person:
    country = "India"

    def __init__(self):
        print("Initializing person...")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing employee...")

    def getSalary(self):
        print("Salary is "+self.salary)
    def takeBreath(self):
        print("I am an employee so I am breathihng...")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print("No salary to programmers.")


p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()

