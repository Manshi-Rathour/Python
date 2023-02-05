class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return str(self.vec[0]) + "i + " + str(self.vec[1]) + "j + " + str(self.vec[2]) + "k"


v = Vector([7, 8, 10])
print(v)
