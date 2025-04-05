a=int(input("Enter first Number"))
b=int(input("Enter Second Number"))
if(b==0):
    raise ZeroDivisionError("The program is Suspended because a number cant be devided by zero\n Thank You")
else:
    print(a/b)
