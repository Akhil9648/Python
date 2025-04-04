class calculator:
    def __init__(self,square,cube,root):
        self.square=square
        self.cube=cube
        self.root=root
    def calculate(self):
        print(f"The squere of the number is {self.square},Cube of the number is {self.cube} and the root of the number is {self.root}")
n=int(input("Enter a number"))
a=calculator(n*n,n*n*n,n*(0.5))
a.calculate()
