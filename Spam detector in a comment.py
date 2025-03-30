# Detect spam in chat
p1="click on this link"
p2="Subscribe"
p3="Buy Now"
p4="Make a lot of money"
message=input("Enter a message:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")
else:
    print("This comment is not a spam")
