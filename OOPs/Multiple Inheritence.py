class Akhil:
    a=1
class pandey(Akhil):
    b=2
class Elite(pandey):
    c=3
o=Akhil()
print(o.a)
# If we print o.b here than it will show error
o=pandey()
print(o.a,o.b)
o=Elite()
print(o.a,o.b,o.c)
