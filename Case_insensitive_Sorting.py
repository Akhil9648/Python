#Case insensitive Sorting
my_string=["Apple","Banana","Kiwi","Orange"]
sorted_strings=sorted(my_string,key=lambda x:x.lower())
print(sorted_strings)
