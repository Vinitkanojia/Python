# Q.1 Calculate the remainder of two numbers.
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# calculate the remainder.
remainder = num1 % num2
print("The remainder of", num1, "and", num2, "is:", remainder)


# Q.2Check if a number is even or odd.
num = int(input("Enter a number:"))

# check if the number is even or odd
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Q.3 Compare two numbers and print the larger one.
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# campare two numbers to find the larder no. .
if num1 > num2 :
    print(num1, "is larger than", num2)
else:
    print(num2, "is larger than", num1) 


# Q.4Write a program to calculate the square and cube of a numbers.
num = int(input("Enter a number:"))

# to calculate the square
sq=num ** 2
print("The square of ", num, "is:", sq)
# to calculate the cube
cube=num ** 3
print("The cube of ", num, "is:", cube)      


# Q.5 check if two entered numbers are equal.
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# usinq if statement to check if two numbers are equal
if num1 == num2:
    print("The two numbers are equal")
else:
    print("The two numbers are not equal")


# Q.6 Take two no. and print true if both are positive , else false.
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# using if statement to check if both numbers are positive.
if num1 > 0 and num2 > 0:
    print("True")
else:
    print("False")


# Q.7 Write a program to convert float to integer.
num = float(input("Enter a float number:"))

# convert float to integer
int_num = int(num)
print("The integer value of", num, "is:", int_num)


# Q.8 Take a no. as string ,convert to int nad multiply by 10.
num=str(input("Enter a number:"))
print(type(num))

# convert string to integer
int_num=int(num)
print(type(int_num))

# multiply by 10
result=int_num*10
print("The result of multiplying", int_num, "by 10 is:", result)


# Q.9 Write a program that uses and & or opeartors to check multiple conditions.
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# using if statement to check if both numbers are positive.
if num1 > 0 and num2 > 0:
    print("Both numbers are positive")

elif num1 > 0 or num2 > 0:
    print("One of the numbers is positive")
else:
    print("Neither number is positive")