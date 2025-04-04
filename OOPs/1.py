class Employee:
    salary=120000 #This is a class attribute
    language="py"

harry=Employee()
harry.name="Harry" #This is an instance attribute
print(harry.name,harry.salary)
rohan=Employee()
rohan.name="Rohan"
print(rohan.name,rohan.salary,rohan.language)
# Here name is instance attribute and salary and language are class attribute as they directly belong to a class
