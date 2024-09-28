# Wap to print multiple table of a given number 

def table(n):
    for i in range(1,11):
        print(f"{n} X {i}= {i*n}")
        i+=1
n=int(input("Enter a number  "))
table(n)