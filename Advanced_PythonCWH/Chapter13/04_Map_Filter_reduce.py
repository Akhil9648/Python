# Map Example
from functools import reduce
l=[4,5,6,7,8]
squere=lambda x:x*x
sqlist=map(squere,l)
print(list(sqlist))

# Filter Example
def even(n):
    if (n%2==0):
        return True
    return False
onlyeven=filter(even,l)
print(list(onlyeven))

# Reduce Example
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
print(reduce(sum,l))
print(reduce(mul,l))
