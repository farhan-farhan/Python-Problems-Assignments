# 1.	An Integer is Input through keyboard. Write a program to find whether it is odd or even number.
# print("hi")
# a=int(input("Enter the Number:\n"))
# if(a%2==0):
#     print(a," is even no ")
# else:
#     print(a,"  is odd no")
      
# 2.	If cost price and selling price of an item is input through keyboard. Write a program to determine how much profit he made or how much loss he got.

# cost_price=float(input("Enter the cost price:"))
# seling_price=float(input("Enter the seling price:"))
# profit=seling_price-cost_price
# loss=cost_price-seling_price
# if(seling_price>cost_price):
#    print("profit= ",profit)
# else:   
#    print("loss = ",loss)
# 3.	WAP to test a number is divisible by 3 or 5 and both.
# n=int(input("Enter the no :"))
# if(n%3==0|n%5==0):
#     print(n," Is divisible by 3 and 5")
# else:
#     print(n," Is NOT divisible by 3 and 5")
       

# 4.	WAP to find the greatest of three numbers entered through keyboard.
# A=int(input("enter A:\n"))
# B=int(input("enter B:\n"))
# C=int(input("enter C:\n"))
# if(A>B and A>C):
#     print(A," is grater Number")
# elif(B>C and B>A):
#     print(B," is grater Number")
# else:    
#        print(C," is grater no")    
      
# 5.The marks obtain by a student in 5 different subjects are input through keyboard. The student gets the division as per the following rules:
# Percentage above or equal to 60- first division
# Percentage between 50 and 59- second division
# Percentage between 40 and 49 – third division
# Percentage below 40- fails.

# print("Enter the max in 5 diffrent sub:\n")
# phy=float(input("Enter the marks in Physic:\n"))
# cem=float(input("Enter the marks in Chemistory:\n"))
# maths=float(input("Enter the marks in Maths:\n"))
# Hindi=float(input("Enter the marks in HINDI:\n"))
# English=float(input("Enter the marks in English:\n"))
# per=(phy+cem+maths+Hindi+English)/5
# print(per,"%")
# if(per>60 and per>=60):
#     print("First division")
# elif(per<60 and per>=50):
#      print("Second Divison")
# elif(per<50 and per>=40):
#     print("third division")
# else :
#     print("fail ")  
               
# 6.	Admission to professional course in a college according to following conditions:
# Marks in Mathematics are greater than or equal to 60 and marks in physics is greater than or equal to 50 and marks in chemistry is greater than or equal to 40
# 			OR
# Total marks in mathematics, physics and chemistry is greater than or equal to 200.
# 					OR
# Total marks in mathematics and physics are greater than or equal to 150.
# Marks of all three subjects will be entered through the keyboard. WAP to tell whether a student is qualifying for admission or not.

# math=int(input("Enter the Marks in Maths:\n"))		
# physics=int(input("Enter the Marks in Physics:\n"))		
# chemistry=int(input("Enter the Marks in chemistry:\n"))	
# if(math>=60 and physics>=50 and chemistry>=40 or math+physics+chemistry>=200 or math+physics+chemistry>=150):
#     print("Student is qulify for Admission:")
# else:
#     print("student is Disqualify for Admission:")
   
    	
# 7.	Write a program that has following menu:
# Enter 1 to find the area of rectangle.
# Enter 2 to find the area of circle.
# Values for length and width of a rectangle and value of a radius of circle will be entered through keyboard.

# option=input("Enter 1 to find the area of rectangle \n Enter 2 to find the area of circle.")
# match option:
#     case "1":
#         l=float(input("Enter the lenght of Rectangle:\n"))
#         w=float(input("Enter the width of Rectangle:\n"))
#         print("Area of Rectangle is : ",l*w)
#     case "2":
#         Radious=float(input("Enter the radious of Circle:"))
#         print("Area of Circule is : ",2*3.14*Radious**2)    
        

# 8.	Write a program that has following menu:
# Enter 1 to find out whether the entered number is even or odd.
# Enter 2 to find out whether the entered number is positive or negative.

# option=int(input(" Enter 1 for even or odd.\n Enter 2 for positive or negative."))
# match option:
#     case 1:
#         num=int(input("Enter the Number:"))
#         if(num%2==0):
#             print(num," is even number")
#         else:
#             print(num," is odd number")
#     case 2:
#         num=int(input("Enter the Number:"))
#         if(num>0):
#             print(num," is positive number")
#         elif(num<0):
#             print(num," is Negaitve number")  
#         else:
#             print(num,"Neaithe positive Nor Negative")    
                
    

# 9. WAP that implements the simple calculator that has following menu:
# Enter 1 to find the addition of two numbers.
# Enter 2 to find the subtraction of two numbers.
# Enter 3 to find the multiplication of two numbers.
# Enter 4 to find the division of two numbers.
# Enter 5 to find the inverse of a number.
# Enter 6 to find the square of a number.
# Enter 7 to find the cube of a number.

# while True:
#  option=input("Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for multiplication.\nEnter 4 for division.\nEnter 5 for inverse.\nEnter 6 for square.\nEnter 7 for cube: \nEnter 8 for Exit")
#  match option:
#       case "1":
#           a=int(input("Enter first No:"))
#           b=int(input("Enter Second No:"))
#           print("Sum of Two number is: ",a+b)
#       case "2":
#           a=int(input("Enter first No:"))
#           b=int(input("Enter Second No:"))
#           print("Sub of Two number is: ",a-b)
#       case "3":
#           a=int(input("Enter first No:"))
#           b=int(input("Enter Second No:"))
#           print("Multiplication of Two number is: ",a*b)   
#       case "4":
#           a=int(input("Enter first No:"))
#           b=int(input("Enter Second No:"))
#           print("Division of Two number is: ",a/b) 
#       case "5": 
#            a=int(input("Enter  No:"))
#            print("Inverse of a number is:",-a) 
            
#       case "6":
#           a=int(input("Enter  No:"))
#           print("Inverse of a number is:",a**2)     
#       case "7": 
#           a=int(input("Enter No:"))
#           print("Inverse of a number is:",a**3)
#       case  "8":
#           break;    
    
    
                 
             


#  10. Write a program that has following menu:
#  Enter code w for withdraw.
#  Enter code d for deposit.
#  Enter code c for checking balance.

# Note: 1 take initial amount as input from user.

# Note:2 You can withdraw an amount only if balance is greater than or equal to 500 and withdrawing amount should be less than balance.

bal=float(input("Enter the initial balance:"))
option=input("Enter code w for withdraw.\nEnter code d for deposit.\nEnter code c for checking balance.")
match option:
    case "d": 
        amt=float(input("Enter the amount to be Diposit:"))
        bal=bal+amt
        print("Update bal is :",bal) 
    case "c":
        print("Avilable balance is: ",bal)
    case "w":
        amt=float(input("Enter amout to be withdrol:"))
        if(bal-500>=amt):
            bal=bal-amt
            print("Updated balcnce is :",bal)
        else:
            print("insufficant balcnce in account or min 500 is not maintained:")
    case _:
        print("INvalid option:")
                    
                    