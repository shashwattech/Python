# https://leetcode.com/problems/reverse-integer/


x = int(input("Enter the integer you want to reverse: "))


def reverseTheInteger(x):

    negativeFlag = 0

    if(x<0):
        negativeFlag = 1
        x= str(abs(x))


    x = str(x)

    reversedNumber = ""

    for i in x:

        reversedNumber = i + reversedNumber

    reversedNumber = int(reversedNumber)
    if (negativeFlag == 1):
        reversedNumber = reversedNumber * (-1)

    return reversedNumber

print(reverseTheInteger(x))





# ------------------- Revision Notes -------------------
# ✅ Step 1: Handle negative numbers using a flag.
# ✅ Step 2: Convert number to string to easily reverse digits.
# ✅ Step 3: Reverse the string manually using a loop.
# ✅ Step 4: Convert reversed string back to integer.
# ✅ Step 5: Reapply the negative sign if necessary.
# ✅ Step 6: Check if the reversed number lies within the 32-bit signed integer range.
# ✅ Step 7: Return 0 if overflow, else return reversed number.
# ------------------------------------------------------




# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """

#         negativeFlag = 0  # Initialize flag to check if input number is negative

#         if(x < 0):
#             negativeFlag = 1             # Set flag if number is negative
#             x = str(abs(x))              # Convert absolute value to string for reversal
#         else:
#             x = str(x)                   # If positive, directly convert to string

#         reversedNumber = ""              # Initialize empty string for reversed digits

#         for i in x:                      # Iterate through each character (digit)
#             reversedNumber = i + reversedNumber  # Build reversed string manually

#         reversedNumber = int(reversedNumber)     # Convert reversed string back to integer

#         if (negativeFlag == 1):                  # Restore negative sign if needed
#             reversedNumber = reversedNumber * (-1)

#         # Check for 32-bit signed integer overflow
#         if reversedNumber > (2**31 - 1) or reversedNumber < -2**31:
#             return 0

#         return reversedNumber  # Return the final reversed number


