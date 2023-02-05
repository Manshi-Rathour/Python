class C2DVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return str(self.icap)+"i+"+str(self.jcap)+"j"

class C3DVec(C2DVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return str(self.icap)+"i+"+str(self.jcap)+"j+"+str(self.kcap)+"k"



V2D = C2DVec(1, 7)
V3D = C3DVec(2, 10, 8)
print(V2D)
print(V3D)

