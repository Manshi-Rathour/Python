class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an employee.")

class Programmer(Employee):
    language = "Python"
    def getLanguage(self):
        print("The language is "+self.language)
    def showDetails(self):
        print("This is a programmer.")


e = Employee()
e.showDetails()
p = Programmer()
p.getLanguage()
p.showDetails()
print(p.company)


