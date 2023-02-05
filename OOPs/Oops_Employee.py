class Employee:
    company = "Google"


harry = Employee()
rajni = Employee()
print(harry.company)
print(rajni.company)

Employee.company = "YouTube"
print(harry.company)
print(rajni.company)

harry.salary = 300
rajni.salary = 400
print(harry.salary)
print(rajni.salary)

