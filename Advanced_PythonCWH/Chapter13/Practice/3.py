from functools import reduce
l=[1,2,5,4,70,80,45,92]
def dev(n):
    if n%5==0:
        return True
    return False
devi=filter(dev,l)
print(list(devi))

# 4th Problem
def maxi(a,b):
    if(a>b):
        return a
    return b
print(reduce(maxi,l))
