n=int(input("Enter The grade:\n"))
if(n>=90):
    print("Grade:A")
elif((n>=80)&(n<=89)):
    print("Grade:B")
elif((70<=n)&(n<=79)):
    print("Grade:C")
elif((60<=n)&(n<=69)):
    print("Grade:D")
elif((50<=n)&(n<=59)):
    print("Grade:E")
elif((40<=n)&(n<=49)):
    print("Grade:F")
else:
    print("Fail!!")
