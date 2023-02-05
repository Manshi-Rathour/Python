class Employee:
    company = "Google"
    eCode = 100

class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Mayank"


p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)

