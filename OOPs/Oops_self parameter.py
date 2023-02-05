class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary for this employee working in "+self.company + " is "+self.salary)


mayank = Employee()
mayank.salary = "10000"
mayank.getSalary()
