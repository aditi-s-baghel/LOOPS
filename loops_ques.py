#                                                   LOOPS QUESTIONS

# 16. Accept an integer and Print hello world n times

n = int(input("enter no of times:"))
for i in range(n):
    print("hello world")


# 17.Print natural number up to n. 

n = int(input("enter num:"))
for i in range(1,n+1):
    print(i)
    

# 18. Reverse for loop. Print n to 1.

n = int(input("enter num:"))
for i in str(n)[n::-1]:
    print(i)
  

# 19. Take a number as input and print its table
#      5 * 1 = 5
#      5 * 2 = 10 ... up to 10 terms

n = int(input("enter a num:"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
   

# 20. Sum up to n terms.

n = int(input("enter num:"))
sum = 0
for i in range(n+1):
    sum += i
print(sum)
 

#21. Factorial of a number

n = int(input("enter a num:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
  

#22. Print the sum of all even & odd numbers in a range seperately.

n = int(input("enter a num:"))
evensum = 0
oddsum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        evensum += i
    else:
        oddsum += i

print(evensum)
print(oddsum)


# 23. Print all the numbers which are either divisible by 3 or 5 in a range

n = int(input("enter a num:"))
for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)


# 24.Print all the factors of a number.

n = int(input("enter a num:"))
for i in range(1,n+1):
    if n % i == 0:
        print(f'factors of n are: {i}')


# 25. Print the sum of all factors of a number, 50 - 1 + 2 + 5 + 10 + 25 = 43

n = int(input("enter a num:"))
factsum = 0
for i in range(1,n):             # n+1 if you want till end
    if n % i == 0:
        factsum += i

print(factsum)


# 26. Accept a number and check if it a perfect number or not.
#     A number whose sum of factors (excluding number itself)  = Number 
#     Ex -  6 = 1, 2, 3 = 6

n = int(input("Enter a number"))
factsum = 0
for i in range(1,n):
    if n % i == 0:
        factsum += i

if factsum == n:
    print("Perfect number")
else:
    print("Not perfect number")
        


# 27. Seprate each digit of a number and print it on the new line

n = int(input("enter num:"))
for i in str(n):
    sep = n % 10
    print(sep)
    n = n//10
  

# without reversing :-

n = int(input("enter number"))
for i in str(n):
    print(i)



# 28. Check if the number is Prime or not.

n = int(input("enter num:"))
count = 0
for i in range(2,n):
    if n % i == 0:
        count += 1

if count == 0:
    print("prime no.")
else:
    print("not prime no.")



#29) Accept a number and print its reverse

n = int(input("enter a num:"))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n//10
print(rev)

# for loop:-

n = int(input("enter a num:"))
for i in str(n)[n::-1]:
    print(i)           



#30) Accept a number and check if it is a palindromic number (If number and its reverse are equal)
 #      Ex - 12321 - Rerverse - 12321


n = int(input("enter a num:"))
copy = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if copy == rev:
    print("palindrome")

else:
    print("not palindrome")

    

# for loop :-

n = int(input("enter a num:"))
copy = n
rev = 0
for i in str(n):
    rev = rev * 10 + n % 10
    n = n // 10

if copy == rev:
    print("palindrome")

else:
    print("not palindrome")