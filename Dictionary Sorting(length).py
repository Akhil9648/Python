#Sorting dictionary on the basisi of key
my_string={'apple':5,'banana':2,'kiwi':8,'orange':3}
sorted_strings=dict(sorted(my_string.items(),key=lambda x:len(x[0])))
print(sorted_strings)
