#Sorting on basis of second value of tuple
my_string=[(2,3),(45,78),(2,3),(9,76),(2,5)]
sorted_strings=sorted(my_string,key=lambda x:x[1])
print(sorted_strings)
