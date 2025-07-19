s = input("Enter the string you want to reverse: ")


def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """


        def checkPalindrome(s):


            reversedString = ""

            for char in s:

                # if char in [' ', ',', ':', '.','@','#','_']:
                #     pass
                # if not char.isalpha():
                #     pass

                if not char.isalnum():
                    pass

                else:
                    reversedString = char.lower() + reversedString


            return reversedString


        string = ''
        for char in s:
            # if char in [' ', ',', ':','.','@','#','_']:
            #     pass
            # if not char.isalpha():
                #     pass

            if not char.isalnum():
                pass
            else:
                string = string + char.lower()
        if (string == checkPalindrome(s)):
            return string == checkPalindrome(s)

        else:
            return string == checkPalindrome(s)
        


# --------------------------- PALINDROME CHECK - CONCEPT NOTES ---------------------------

# 🎯 GOAL:
#   Check if a string is a valid palindrome after removing non-alphanumeric characters
#   and ignoring case sensitivity.

# 🔤 DEFINITIONS:
# - Palindrome: A string that reads the same forwards and backwards (e.g., "madam", "121")
# - Alphanumeric: Characters that are either letters (A–Z, a–z) or digits (0–9)

# 🔍 STEP-BY-STEP STRATEGY:
# 1. Clean the input string:
#    - Remove all characters that are NOT alphanumeric using `char.isalnum()`
#    - Convert each character to lowercase using `.lower()`

# 2. Build two strings:
#    - `string`: normal cleaned version
#    - `reversedString`: reverse of the cleaned version

# 3. Compare both. If equal → it's a palindrome.

# ✅ USEFUL FUNCTIONS:
# - char.isalnum(): Returns True if char is A–Z, a–z, or 0–9
# - char.lower(): Converts any uppercase letter to lowercase
# - s[::-1]: Reverses a string

# ❌ COMMON MISTAKES TO AVOID:
# - Using `char.isalpha()` instead of `char.isalnum()` → skips digits!
# - Comparing string without cleaning → wrong output
# - Using `print()` instead of `return` in LeetCode
# - Repeating expensive function calls (like `checkPalindrome(s)`) multiple times

# 🧠 FUTURE OPTIMIZATION (not required now):
# - Use two-pointer technique to compare start and end directly without reversing
# ----------------------------------------------------------------------------------------




# s = input("Enter the string you want to reverse: ")  # ❗️Input taken, but not used in this function

# def isPalindrome(self, s):  # ⚠️ This method assumes it's part of a class (LeetCode format)

#         def checkPalindrome(s):
#             reversedString = ""
#             for char in s:
#                 # ❌ Don't hardcode symbols — use isalnum()
#                 # ✅ Good: using char.isalnum() to skip unwanted characters

#                 if not char.isalnum():
#                     pass  # ✅ Skips symbols, whitespace, etc.
#                 else:
#                     reversedString = char.lower() + reversedString  # ✅ Builds reversed string cleanly

#             return reversedString  # ✅ Returns the cleaned + reversed string

#         string = ''
#         for char in s:
#             if not char.isalnum():
#                 pass
#             else:
#                 string = string + char.lower()  # ✅ Builds cleaned version of input string

#         # ❗️Redundant check: you are calling checkPalindrome(s) twice unnecessarily
#         # You could simplify:
#         #    return string == checkPalindrome(s)

#         if (string == checkPalindrome(s)):
#             return string == checkPalindrome(s)  # ❗️Redundant condition
#         else:
#             return string == checkPalindrome(s)  # ❗️Same line repeated — wasteful

# # ❌ You're not calling isPalindrome(s) with the input 's' at the end of your program
# # If you want to run it directly, add:
# # print(isPalindrome(None, s))  # Passing None for 'self' (outside class)

# # OR:
# # Make it a standalone function (remove 'self') if you're not running it in LeetCode class format
