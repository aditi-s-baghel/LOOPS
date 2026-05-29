# 1. Ask the user to enter a number and print all prime numbers up to that number

n = int(input("Enter a number:"))
for a in range(1,n+1):
    count = 0

    for i in range(1,a+1):
        if a % i == 0:
            count += 1

    if count == 2:
        print(a)


# 2. Ask the user to enter a number and check if it is Armstrong number

n = int(input("Enter a num:"))
copy = n
length = len(str(n))
sum = 0
for i in range(n):
    digit = n % 10
    sum = sum + digit ** length
    n = n // 10

if copy == sum:
    print("Armstrong no.")
    
else:
    print("Not an Armstrong no.")   


# 3. Ask the user to enter a number and print the sum of digits using loop

n = int(input("Enter a number:"))
sum = 0
for i in str(n):
    sum = sum + int(i)
print(sum)          


# 4. Ask the user to enter a number and print reverse of the number

n = int(input("Enter a number:"))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print(rev)
            
#                                            OR

n = int(input("Enter a number:"))
digit = " "
for i in str(n)[::-1]:
    digit = digit + i

print(digit)


# 5. Ask the user to enter a number and check if it is palindrome

n = int(input("Enter a number:"))
copy = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10 
    n = n // 10

if copy == rev:
    print("palindrome")

else:
    print("not palindrome")

#                                            OR

n = int(input("Enter a number:"))
copy = n
rev = 0
length = len(str(n))
for i in range(length):
    rev = rev * 10 + n % 10 
    n = n // 10

if copy == rev:
    print("palindrome")

else:
    print("not palindrome") 



# 6. Ask the user to enter a number and print all numbers between 1 to n that are divisible
#    by both 3 and 5.

n = int(input("Enter a number:"))
for i in range(n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)                                        



# 7. Ask the user to enter a number and print factorial using loop without using built-in
#    functions


n = int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
    fact *= i

print(fact)