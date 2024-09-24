
#Find the greatest among four numbers entered by user 

n1=int(input("Enter first number:"))
n2=int(input("Enter Second number:"))
n3=int(input("Enter  third number:"))
n4=int(input("Enter fourth number:"))

if(n1>n2 and n1>n3 and n1>n4):
    print("Greastest number is",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("Greatest number is:",n2)
elif(n3>n1 and n3>n2 and n3>n4):
    print("Greatest number is:",n3)
elif(n4>n1 and n4>n2 and n4>n3):
    print("Greatest number is:",n4)

    