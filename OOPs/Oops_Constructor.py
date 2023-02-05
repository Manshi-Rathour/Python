class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print("Name of the employee is "+self.name)
        print("Salary is "+self.salary)
        print("Subunit is "+self.subunit)


mayank = Employee("Mayank", "100000", "YouTube")
mayank.getDetails()
