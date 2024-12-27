def f():
    print("Hello!!")
print(f())
print(type(f()))
x=(0,False,True,2,4,5)
x1={0:1,False:'a','b':True,1:{2,3,5,1}}
# x2={{1,2}:{1,2}}
y={1,2,3,4,5}
print(x1)
print(type(x1))
for i in x1.items():
    print(i)
l1=[1,2,3,[4,5]]
l2=l1[:]
l4=l1.copy
print(id(l1[3]),id(l2[3]))
def f1(y,x):
    print(x,y)
f1(x=3,y=4)
f1(y=2,x=5)
    
