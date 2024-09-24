# Wap to find wether a student has passed or failed if it required 33% in each subject and 40% OVERALL marks 



s1=float(input("Enter your marks in Subject 1:"))
s2=float(input("Enter your marks in Subject 2:"))
s3=float(input("Enter your marks in Subject 3:"))

total_percentage=((s1+s2+s3)/300)*100



if(s1>=33 and s2>=33 and s3>=33 and total_percentage>=40):
    print(f"Congratulations <-- You are Passed --> With",total_percentage, "%")
else:
    print(f"<--You are failed--> With",total_percentage ,"%" "\t Try again next year!")   



# Grading 

if(total_percentage>=0 and total_percentage<=39.99) :
    print("Your grade is 'F' ")
elif(total_percentage>=40 and total_percentage<=44.99) :
    print("Your grade is 'P' ")
elif(total_percentage>=45 and total_percentage<=54.99) :
    print("Your grade is 'C' ")
elif(total_percentage>=55 and total_percentage<=64.99) :
    print("Your grade is 'B' ")
elif(total_percentage>=65 and total_percentage<=74.99) :
   print("Your grade is 'B+' ")
elif(total_percentage>=75 and total_percentage<=84.99) :
    print("Your grade is 'A' ")
elif(total_percentage>=85 and total_percentage<=94.99) :
    print("Your grade is 'A+' ")
elif(total_percentage>=95 and total_percentage<=100) :
    print("Your grade is 'O' ")