class Calculator:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def greet():
        print("HELLO!")

    def square(self):
        print("square is "+str(self.num ** 2))

    def cube(self):
        print("cube is "+str(self.num ** 3))


num = Calculator(3)
num.greet()
num.square()
num.cube()
