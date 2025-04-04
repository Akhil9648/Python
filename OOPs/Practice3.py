class Demo:
    a=4
o=Demo()
print(o.a) #Prints the class attribute because instance attribute is not present
o.a=0  #instance attribute set
print(o.a) #prints the instance attribue
print(Demo.a) #Prints the class attribute

# Hence the Class attrubute is not chaged
