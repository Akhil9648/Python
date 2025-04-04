import random
n=random.randint(1,100)
count=0
a=int(input("Guess the Number"))
while(a!=n):
    if(a>n):
        print("You Guessed a larger Number")
    elif(a<n):
        print("You Guessed a smaller Number")
    a=int(input("Guess the Number"))
    count+=1
print(f"Yay! You did it\nYou Guessed {n},Your Score is {count}")
