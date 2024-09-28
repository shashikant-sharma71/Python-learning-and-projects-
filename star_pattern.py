
# # Wap to print to following pattern 

# ''' 
#            *
#           ***
#          ***** 
 

#                '''

n = int(input("Enter the value of n"))
for i in range(1,n+1):
    print("   "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print(" ")



#   # Wap to print to following pattern 

# '''
#          ***
#          * *
#          ***
#                  '''
# n= int(input("Enter the value of n :"))   
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n ,end="")
#         print(" ")

#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#         print(" ")


# Wap to print to following pattern 

# '''
#          1
#          123
#          1234
#          12345

#                  '''

# n=int(input("Enter a number"))

# for i in range(1,n):
#     print("1")
#     print("*"*(n),end="")


