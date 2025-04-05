try:
    with open("a.txt","r") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("b.txt","r") as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open("c.txt","r") as f3:
        print(f3.read())
except Exception as e:
    print(e)
finally:
    print("Thank You")
