f=open("C:\\File_handling_python\\numbers.txt",'r')
x=f.read().split()
x.sort()
print(x)
f.close()
for i in x:
    print(i)
