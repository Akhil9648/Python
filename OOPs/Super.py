class Akhil:
    def __init__(self):
        print("Constructor of Akhil")
    a=1
class pandey(Akhil):
    def __init__(self):
        super().__init__()
        print("Constructor of pandey")
    b=2
class Elite(pandey):
    def __init__(self):
        super().__init__()
        print("Constructor of Elite")
    c=3
o=Akhil()
print(o.a)
# If we print o.b here than it will show error
o=pandey()
print(o.a,o.b)
o=Elite()
print(o.a,o.b,o.c)
