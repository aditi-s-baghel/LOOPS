# 1) Accept numbers from a user

n = int(input("Enter numbers:")) 
print(n)


# 2) Display three string “Name”, “Is”, “James” as “Name**Is**James”

print("Name","Is","James", sep = "**")


# 3) Display float number with 2 decimal places using print()

n = 45.6789
print ("%.2f" % n)  


# 4) Sum of two integers

a = 4
b = 5
sum = a + b
print(sum) 


# 5) Accept two integers from user and print the sum
#    Ex - The sum of 45 & 12 = 57


n1 = int(input("enter num1:"))
n2 = int(input("enter num2:"))
sum = n1 + n2
print(sum)                                             


# 6) Accept the User's name, age and print in following manner
#    Ex - Hello Shery, you are 12 years old.

name = input("Enter user's name:")
age = int(input("Enter user's age:"))
print(f"Hello {name} you are {age} years old")



# 7.Take 3 int inputs from user and check and print the result.
#   all are equal, any of two are equal( use and, or )

n1 = int(input("enter n1:"))
n2 = int(input("enter n2:"))
n3 = int(input("enter n3:"))

if n1 == n2 and n1 == n3:
    print("All are equal")
else:
    print("All are not equal")  



# 8 . Accept two numbers and print the greatest between them

n1 = int(input("enter n1:"))
n2 = int(input("enter n2:"))
if n1 > n2:
    print("n1 is greatest")
else:
    print("n2 is greatest") 



# 9. Accept the gender from the user as char and print the respective greeting message
#    Ex - Good Morning Sir (on the basis of gender)

gender = input("Input gender- M/F:")

if gender == "M":
    print("Good Morning Sir")

elif gender == "F":
    print("Good Morning Mam")

else:
    print("Invalid Gender")   



# 10. Extend the previous program and handle the wrong inputs.
#     Print Good Morning sir for input m or M & Good morning Maam for input F or f 
#     else print Wrong Input

gender = input("Input gender- M,m/F,f:")

if gender == "M" or gender == "m":
    print("Good Morning Sir")

elif gender == "F" or gender == "f":
    print("Good Morning Mam")

else:
    print("Invalid Gender")  



# 11. Accept an integer and check whether it is an even number or odd.

n = int(input("enter a num:"))
if n % 2 == 0:
    print("even number")
else:
    print("odd number")     



# 12. Accept name and age from the user. Check if the user is a valid voter or not.
   #   Vaid - Hello Shery, You are a valid voter.
    #  Invalid - Sorry Shery, you can't cast the vote.
	#Part 2 - Print after how many years the user will be eligible

name = input("enter name:")
age = int(input("enter age:"))

if age >= 18:
    print("Hello" ,name ,"You are a valid voter.")

else:
    print("Sorry" ,name, "you can't cast the vote.")

years_left = 18 - age

print("you will be eligible after:",years_left ,"years")   



# 13. Accept the parameters and calculate the Compound Interest & print it on STDOUT (Use Math class methods)

import math
p = float(input("enter principal amount: "))
r = float(input("enter rate of interest: "))
t = int(input("enter time(in years): "))

amount = p * math.pow((1+r/100),t)
CI = amount - p
print(CI)   



#14) Accept a year and check if it a leap year or not 

year = int(input("enter year:"))
if year % 4 == 0 and year % 100 != 0:
    print("leap year")
else:
    print("not a leap year")
                                                                   


#15) Accept an english alphabet from user and check if it is a consonant or a vowel

alpha = input("enter an alphabet:")

if alpha in "aeiouAEIOU":
    print("alphabet is vowel")
else:
    print("alphabet is consonant")