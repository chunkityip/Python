"""
Factorial
Write a program that takes a number as input and prints its factorial.
"""
# def factorial(num):
#     if num < 0: return f"{num} is not defined for negative numbers."
#     if num == 0 or num == 1: return 1
#
#     result = 0
#     for i in range(2 , num + 1):
#         result *= i
#     return result
#
# num = int(input("Enter a number: "))
#
# # Calculating the factorial using the factorial function
# result = factorial(num)
#
# # Printing the factorial
# print(f"The factorial of {num} is {result}")


"""
Palindrome
Write a program that checks if a given string is a palindrome.
"""
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    left, right = 0, len(s) - 1

    while left < right:
        # .isalnum() checks if it is a letter (a-z) or number (0-9)
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

