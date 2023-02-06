#Write a programme to check whether a number is divisible by 5,7,11

num = int(input("enter a number:"))
if (num%5 == 0):
 print("the number is divisible by 5")
else :
 print("not divisible")

num = int(input("enter a number:"))
if (num%2 == 0):
print("the number is even")
else :
print("not divisible")


#write aprogram to assign a discount of 5% if amount of purchase exceeds sh 1000

amount_purchased = float(input("enter amount purchased:"))
if (amount_purchased >1000):

    discount = 0.005*amount_purchased 
    print("discount offered is ", discount)
else:
    print("no discount")
   
#write a program to check if a person is eligible to vote.the person must be a kenyan citizen and above 18years
age = int(input("Enter the age"))
citizenship = str(input("Enter your citizenship:"))
if(age >= 18) and (citizenship == "kenyan"):
 print("you are eligible to vote")
else:
    print("you are not eligible to vote")

citizenship = str(input("Enter your citizenship:")).lower()
if(citizenship == "kenyan"):
 print("you are eligible to vote")
else:
    print("you are not eligible to vote")


#write a computer program to implement the following
#Requirements -A bank will offer a customer a loan if they are 21 or over and have an annual income of atleastsh 21,000
# the customers age and income are input in response to user friendly prompts.write a program that will output the 
# following:  1.congratulations you qualify for a loan.
# 2.unfortunately, we are unable to offer you a loan this time.
 
annual_income = int(input("Enter your annual income:"))
age = int(input("Enter your age:"))
if(annual_income >= 21000) and (age >= 21):
 print("congratulations you qualify for a loan")
else:
    print("unfortunately, we are unable to offer you a loan this time.")

    #write a program to check if you are eligible to vote:
    #conditions : must be an Esat African citizen (kenya,Uganda,Tanzania) and above 18 years.

EastC = ["Kenya", "Uganda", "Tanzania"]
age = int(input("Enter your age:"))
country = str(input("Enter your country:")).lower()
if (country in EastC) and (age >= 18):
 print("you are eligible to vote")
else:
            print("you are not eligible to vote")

