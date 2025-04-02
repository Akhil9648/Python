def calculate(cp,sp):
    profit=sp-cp
    return profit
cp=float(input("Give the Cost Price:"))
sp=float(input("Give the selling price:"))
profit=calculate(cp,sp)
print(f"Cost Price is:{cp},Selling Price is:{sp} and the profit earned is {profit}")
