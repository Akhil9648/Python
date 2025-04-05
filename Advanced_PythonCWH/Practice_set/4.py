a=int(input("Enter first Number"))
b=int(input("Enter second Number"))
try:
    print(a/b)
except Exception as e:
    print("∞")
finally:
    print("Thanks")
