#Sorting dictionary on the basis of key
my_string={'apple':5,'banana':2,'kiwi':8,'orange':3}
sorted_strings=dict(sorted(my_string.items(),key=lambda x:x[1]))
print(sorted_strings)
