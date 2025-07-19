s = input("Enter the sting you want to count vowel for : ")


def countVowels(s):

    vowels = "aeiouAEIOU"
    vowelCount = 0


    for char in s:

        if char in vowels:

            vowelCount = vowelCount +1

    
    return vowelCount


print(countVowels(s))





# s = input("Enter the string you want to count vowels for: ")

# def countVowels(s):

#     vowels = "aeiouAEIOU"        # ✅ Include both lowercase and uppercase vowels
#     vowelCount = 0               # ✅ Counter variable to track total vowels

#     for char in s:               # ✅ Loop through each character in the string

#         if char in vowels:       # ✅ If character is a vowel (match in the string)
#             vowelCount += 1      # ✅ Increment the vowel counter

#     return vowelCount            # ✅ Return total count

# print(countVowels(s))            # ✅ Call the function and print result




"""
Problem: Count Vowels in a String

Concepts Covered:
-----------------
1. **Looping Through Strings** – Iterate one character at a time using a `for` loop.
2. **String Membership (`in`)** – Check if a character exists in a list or string using `in`.
3. **Counting Logic** – Use a counter variable and increase it conditionally.
4. **Case Sensitivity** – Vowels can be lowercase or uppercase. Either:
   - Include both cases in the `vowels` string, OR
   - Convert input to lowercase using `s = s.lower()`.
5. **Function Definition** – Encapsulate logic inside a function for reuse.
6. **Clean Output** – Print the return value directly from the function.
"""


