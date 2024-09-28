#Wap to convert into calcius to faranhite 

'''
formila= c/5=f-32/9

'''

# c=5*(f-32)/9
def calcious(f):
   return 5*(f-32)/9
f=int(input("Enter temprature in F: "))
print(f"{round(calcious(f),2)}°C")








