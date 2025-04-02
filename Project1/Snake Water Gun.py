import random
comp=random.choice([-1,0,1])
you=int(input("Enter a number between 1 for Snake,0 For Water,-1 for Gun:"))
if(you>1 or you<-1):
    print("Something Went Wrong")
    exit(0)
youdict={1:"Snake",0:"Water",-1:"Gun"}
print(f"You chose:{youdict[you]} and Computer chose:{youdict[comp]}")
if comp==you:
    print("Its a Draw")
else:
    if (comp==1 and you==-1):
        print("You Win")
    elif (comp==1 and you==0):
        print("You Lose")
    elif (comp==0 and you==-1):
        print("You Lose")
    elif (comp==0 and you==1):
        print("You Win")
    elif (comp==-1 and you==0):
        print("You Lose")
    elif (comp==-1 and you==1):
        print("You Win")
    else:
        print("Something Went Wrong")
