"""
1. Print "Hello, World!"
Write a program to print "Hello, World!" to the console.
"""
print("Hello World")

"""
2. Simple Arithmetic
Create a program that takes two numbers as input and 
prints their sum, subtraction, multiplication, and division.
"""
def sum (num , num1):
    return num + num1

def subtraction(num , num1):
    return num - num1

def multiplication(num , num1):
    return num * num1

def division(num , num1):
    return num / num1

num = int(input("Enter a number: "))
num1 = int(input("Enter another number: "))
print(sum(num , num1))
print(subtraction(num , num1))
print(multiplication(num , num1))
print(division(num , num1))

"""
3. Odd or Even
Write a program to check if a number is odd or even.
"""
def checkNum(num):
    if (num % 2 == 0):
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")

num = int(input("Enter a number: "))
checkNum(num)

"""
4. Largest of Three Numbers
Write a program that takes three numbers as input and prints the largest number.
"""
def checkLargest(num1 , num2 , num3):
    compare = num1 if num1 > num2 else num2
    return num3 if num3 > compare else compare

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

print(f"{checkLargest(num1 , num2 , num3)} is the largest number")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

print(f"{max(num1 , num2 , num3)} is the largest number")

"""
5. Simple Calculator
Write a program that takes two numbers and 
an operator (+, -, *, /) as input and performs the corresponding operation.
"""

def sum(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2

def multipy(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

print(sum(num1, num2))
print(subtract(num1, num2))
print(multipy(num1, num2))
print(divide(num1, num2))
