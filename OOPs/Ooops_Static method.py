class Employee:
    company = "Google"
    def getSalary(self, name):
        print("Salary for this employee working in "+self.company + " is "+self.salary+"\n"+name)

    @staticmethod
    def greet():
        print("Good Morning, sir!")

mayank = Employee()
mayank.salary = "10000"
mayank.getSalary("Mayank Rathour")
mayank.greet()

