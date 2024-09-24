list=["Shashi","Abhi","Mohit","Sohan"]
print(type(list))

name=input("Enter the name that you want to found: ")

if(name in list):
    print("Your name is in the list")
else:
    print("Your name is not in the list")