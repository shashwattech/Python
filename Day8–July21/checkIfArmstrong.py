x = int(input("Enter the number you want to check is armstrong: "))



def checkArmstrong(x):
    original = x
    x = str(x)
    y = len(x)
    sum = 0

    for digit in x:

        sum = sum + (int(digit) ** y)

    if (original == sum):

        return True
    else:

        return False
    

    
print(checkArmstrong(x))





# Armstrong Number:
# A number is an Armstrong number if the sum of its digits each raised to the
# power of the number of digits equals the original number.

# Example:
# 153 → 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 → ✅ Armstrong
# 123 → 1^3 + 2^3 + 3^3 = 36 → ❌ Not Armstrong

# Steps:
# 1. Store original number (needed for final comparison).
# 2. Convert number to string to loop through digits.
# 3. Count digits using len().
# 4. For each digit → raise to the power of total digits and sum it.
# 5. If sum equals original number → return True.
