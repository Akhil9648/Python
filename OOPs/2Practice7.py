class vector:
    def __init__(self,l):
        self.l=l
    def __len__(self):
        return len(self.l)
c1=vector([2,3,4])
print(len(c1))
