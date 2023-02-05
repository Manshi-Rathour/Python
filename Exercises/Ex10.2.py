class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print("Square is "+str(self.num ** 2))

    def squareRoot(self):
        print("squareRoot is "+str(self.num ** 0.5))

    def cube(self):
        print("Cube is "+str(self.num ** 3))


a = Calculator(4)
a.square()
a.squareRoot()
a.cube()


