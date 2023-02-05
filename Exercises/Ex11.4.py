# (a+bi)(c+di) = (ac-bd)+(ad+bc)i
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.img = i

    def __add__(self, c):
        return Complex(self.real+c.real, self.img+c.img)

    def __mul__(self, c):
        mulReal = self.real*c.real - self.img*c.img
        mulImg = self.real*c.img + self.img*c.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        return str(self.real)+"+" + str(self.img)+"i"


c1 = Complex(1, 4)
c2 = Complex(5, 3)
print(c1 + c2)
print(c1 * c2)

