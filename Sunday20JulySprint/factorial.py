x = int(input("Ente rthe number for which you want the factorial for: "))


def factorial(x):

    if x == 0 or x == 1:

        return 1
    

    factorial = 1

    for i in range (2, x+1):

        factorial = factorial * i


    return factorial


print (factorial(x))



# FACTORIAL CONCEPT NOTES:
# -------------------------
# - Factorial of a number n is the product of all positive integers ≤ n.
# - factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
# - By definition:
#     factorial(0) = 1
#     factorial(1) = 1
#
# - Used in combinations, permutations, recursive problems, etc.
# - Typical interview questions:
#     - Calculate factorial using iteration ✅
#     - Calculate using recursion
#     - Count trailing zeros in n! (LeetCode 172)
