#sorting based on last character
my_string=["apple","banana","kiwi","orange"]
sorted_strings=sorted(my_string,key=lambda x:len(x))
print(sorted_strings)
