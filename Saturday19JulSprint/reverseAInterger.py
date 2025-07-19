
x = int(input("Enter an integer to be reversed: " ))


def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """

    negativeFlag = 0  # ✅ Flag to check if original number was negative

    if x < 0:
        x = abs(x)           # ✅ Work with absolute value for reversal
        negativeFlag = 1     # ✅ Mark that the number was negative

    y = str(x)               # ✅ Convert number to string for reversal
    z = y[::-1]              # ✅ Reverse string using slicing

    z = int(z)               # ✅ Convert reversed string back to integer

    if z > (2**31 - 1):      # ❗ Handle overflow case for 32-bit integer
        return 0             # ⛔ If overflow, return 0 as per LeetCode constraint

    if negativeFlag == 1:
        z = z * -1           # ✅ Reapply negative sign if it was negative

    return z                 # ✅ Return final reversed integer



print(reverse(x)) 


# 📌 Python slicing: str[::-1] reverses a string
# 📌 abs(x) gives absolute value — used to ignore sign before reversing
# 📌 int(str) converts a string to integer (but crashes if invalid like "321-")
# 📌 You MUST check overflow when reversing numbers in LeetCode problems
# 📌 32-bit signed int range = -2147483648 to 2147483647
# 📌 Use flag variables for sign handling — clean and readable
# ❌ Don’t write: x = abs(x) and negativeFlag = 1  ← invalid Python
# ❌ Don’t forget to check: if reversed_int > 2**31 - 1 ← causes runtime error
# ❌ Don’t return string instead of integer
# ❌ Don’t reuse input variable as loop/index




#SLICING CONCEPTS:
# 📌 s[::1] → full string, forward direction (default behavior)
# 📌 s[::-1] → full string, reversed
# 📌 s[1::] → start from index 1 to end
# 📌 s[:3:] → start from beginning, go till index 3 (exclusive)
# 📌 s[::2] → every 2nd character from start to end