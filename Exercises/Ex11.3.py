class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sal):
        self.increment = sal/self.salary


e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 3000
print(e.increment)
print(e.salary)
print(e.salaryAfterIncrement)





