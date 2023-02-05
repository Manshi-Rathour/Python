class Employee:
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getInfo(self):
        print("Name of the employee is "+self.name + " and the salary is "+self.salary)


Manshi = Employee("Manshi", "100k")
Ananya = Employee("Ananya", "90k")
Manshi.getInfo()
Ananya.getInfo()

