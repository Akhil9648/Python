class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,c2):
        return vector(self.i+c2.i,self.j+c2.j,self.k+c2.k)
    def __str__(self):
        return f"{self.i}+{self.j}j+{self.k}k"
c1=vector(2,3,4)
print(c1)
