def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
a=sum(int(input("Enter a number")))
print(a)
