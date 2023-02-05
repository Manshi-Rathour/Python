class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
print(harry.salary)
print(rajni.salary)

harry.salary = 300          # creating an instance attribute
rajni.salary = 400
print(harry.salary)
print(rajni.salary)

# print(rajni.address)      # this line throws an error as address is not present ininstance/class
