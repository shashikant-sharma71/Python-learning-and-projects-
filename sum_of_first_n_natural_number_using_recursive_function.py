def sum_natural_number(n):
   if(n==1):
      return 1
   return sum_natural_number(n-1)+n

#Driver Code 

n=int(input("Enter a numbe: "))
print(f"Sum of the number of term is: {sum_natural_number(n)}")