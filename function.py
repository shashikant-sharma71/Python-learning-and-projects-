# #Write a program to greet a user with "Good Day"using function 

# def greet(name,ending):
#     print("Good Morning!",name)
#     print(ending)

# greet("Shashikant","Thank you.")
# greet("Nitish","Thank you.")
# greet("Mohit ","Thank you.")
# greet("Chandan","Thank you.")
# greet("Abhishek","Thanks.")

# Recursion 
#  It call itself 
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n =int(input("enter a number "))
print(f"factorial of {n} =",factorial(n)) 