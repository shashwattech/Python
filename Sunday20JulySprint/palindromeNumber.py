# https://leetcode.com/problems/palindrome-number

x= 121

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if (x<0):
        return False

    y = str(x)


    def reverseTheNumber(y):
        reverseNumber = ""

        for i in y:

            reverseNumber = i + reverseNumber

        
        return reverseNumber

    
    if (int(reverseTheNumber(y)) == x):

        return True
    else:
        return False
    

print (isPalindrome(x))


# ✅ PROBLEM: Check if a number is a palindrome (LeetCode 9)
# A number is a palindrome if it reads the same backward and forward (e.g. 121, 12321).
# We ignore negative numbers, as they can't be palindromes due to the '-' sign.
# STRATEGY:
# - Convert number to string
# - Reverse the string
# - Convert reversed string back to int and compare with original number
# If same, return True; else return False
# NOTE: Don't use `self` unless writing inside a class method.


# # Define the input number
# x = 121

# # Define the function
# def isPalindrome(x):
#     # Palindromes can't be negative
#     if x < 0:
#         return False

#     # Convert the integer to string to reverse it
#     y = str(x)

#     # Define an inner function to reverse the string
#     def reverseTheNumber(y):
#         reverseNumber = ""  # Initialize empty string
#         for i in y:
#             reverseNumber = i + reverseNumber  # Reverse logic: build from the front
#         return reverseNumber

#     # Compare the reversed number (as int) with the original
#     return int(reverseTheNumber(y)) == x

# # Call the function and print the result
# print(isPalindrome(x))  # Expected Output: True