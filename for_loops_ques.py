# 1. Ask the user to enter a number and print sum of first n natural numbers.

n = int(input("Enter a number:"))
sum = 0
for i in range(n+1):
    sum += i
print(sum)


# 2. Ask the user to enter a number and print factorial of that number.

n = int(input("enter a no.:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)


# 3. Ask the user to enter a number and print all even numbers up to that number

n = int(input("Enter a number:"))
for i in range (n+1):
    if i % 2 == 0:
       print(f'even numbers are {i}')


# 4. Ask the user to enter a number and print all odd numbers up to that number

n = int(input("enter a number:"))
for i in range (n+1):
    if i % 2 != 0 :
        print(f'odd numbers are {i}')


# 5. Ask the user to enter a number and print numbers divisible by 5 up to that number

n = int(input("Enter a number:"))
for i in range(n+1):
    if i % 5 == 0:
        print (i)


# 6. Ask the user to enter a number and print the sum of even numbers up to that number

n = int(input("enter an number:"))
sum = 0
for i in range(n+1):
    if i % 2 == 0:
        sum += i
print(sum)


# 7. Ask the user to enter a number and print the product of numbers from 1 to n

n = int(input("Enter a no.:"))
product = 1
for i in range(1,n+1):
    product *= i
print(product)


# 8. Ask the user to enter a number and print squares of numbers from 1 to n

n = int(input("Enter a number:"))
for i in range(1,n+1):
    print(i*i)


# 9. Ask the user to enter a number and print sum of odd numbers up to n

n = int(input("enter a number"))
sum = 0
for i in range (1,n+1):
    if i % 2 != 0:
        sum += i
print(sum)


# 10. Ask the user to enter a number and print reverse of that number using loop

n = int(input("Enter a number:"))
for i in range(n-1,0,-1):
    print(i)
    