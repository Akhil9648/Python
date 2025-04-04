class Twodvec:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vector is {self.i} {self.j}")
class threedvec(Twodvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The vector is {self.i} {self.j} {self.k}")
o=Twodvec(1,2)
o.show()
p=threedvec(1,2,3)
p.show()
