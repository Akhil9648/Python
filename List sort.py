# Enter the marks of n students and print them in sorted order
n=int(input("Enter the number of students"))
fruits=[]
for i in range (n):
    name=input("Enter marks here:")
    fruits.append(name)
fruits.sort()
print(fruits)
