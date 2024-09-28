# Wap to print greatest of three number using function 


def greatest(a,b,c):
    if(a>b and b>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c


a=int(input("Enter first number:"))

b=int(input("Enter Second number:"))

c=int(input("Enter Third number:"))


print(greatest(a,b,c))


