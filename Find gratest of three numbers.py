def fun():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=int(input("Enter a number: "))
    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>a:
        if b>c:
            return b
        else:
            return c
    else:
        return c
a=fun()
print(a)
