"""
1. Print "Hello, World!"
Write a program to print "Hello, World!" to the console.
"""
# print("Hello World")

"""
2. Simple Arithmetic
Create a program that takes two numbers as input and 
prints their sum, subtraction, multiplication, and division.
"""
# def sum (num , num1):
#     return num + num1

# def subtraction(num , num1):
#     return num - num1

# def multiplication(num , num1):
#     return num * num1

# def division(num , num1):
#     return num / num1

# num = int(input("Enter a number: "))
# num1 = int(input("Enter another number: "))
# print(sum(num , num1))
# print(subtraction(num , num1))
# print(multiplication(num , num1))
# print(division(num , num1))

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