class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
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
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
