# Write a program to print your name ,age and city in one line.

name = "Vinit Kanojia"
age = 20
city = "Valsad"

# To print the name, age and city in one line
print("My name is",name,". I am",age,"years old and I live in",city,".")

#2
# Take  user input for two no. and print their sum.
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# sum of two numbers
sum = num1 + num2
print ("The sum of Two Numbers is :",sum)

#3
# Write a program to convert temperature from Celsius to Fahrenheit
temp_celsius=30
# Formula to convert Celsius to Fahrenheit
temp_fahrenheit=(temp_celsius * 9/5) + 32
print("Temperature in Fahrenheit is:",temp_fahrenheit)

#4
# Store your name in a variable and print it in upper case.
name=str(input("Enter your name:"))
print(name)

# print the name in upper case
uppercase=name.upper()
print("Your name in uppercase :",uppercase)

#5
# Ask the user for their birth year and print their current age.
birth_year=int(input("Enter your Birth year :"))
# Calculate the current age
current_age = 2026 - birth_year
print("Your current age is:",current_age)

#6
# Write a program to swap the values of two variables.
a=10
b=20
# Swapping the values of a and b
#before swapping
print("Before swapping:")
print("a =",a)
print("b =",b)
a,b=b,a
#After swapping
print("After swapping: ")
print("a =",a)
print("b =",b)

#7
# Create a program to calculate the area of a rectangle from the user inputs
a=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
# formula of Area of rectangle area=a*b
c=a*b
print("Area of rectangle is:",c)

#8
#Check whether the no. is positive or negative
a=int(input("Enter a number:"))

#check for positive or negative
if a>0:
    print("The number is positive")
elif a<0:
    print("The number is negative")
else:
    print("The number is zero")

#9
# Ask for two no. and print their average.
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# average of two numbers
average = (num1 + num2) / 2
print ("The average of Two Numbers is :",average)