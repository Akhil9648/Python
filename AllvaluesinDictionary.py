# WAP to display key value of given items for given items
fruits={"Apple":120,"Banana":50,"Orange":100,"Pomogranate":200}
items=fruits.items()
print(items)
for i in fruits:
    print(f"{i}:{fruits[i]}")
for i,j in fruits.items():
    print(i,j)