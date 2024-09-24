p1="Make a lot of money"
p2="buy now"
p3="Subscribe now"
p4="Click this"

massage=input("Enter your Comment")

if(p1 in massage  or p2 in massage or  p3 in massage  or p4 in massage):
    print("This comment is spam")
else:
    print("This is not a spam comment")