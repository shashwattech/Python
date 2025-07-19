num = int(input("Enter the number you want to print: "))  # ✅ INPUT: Correct use of int()

def fib(num):
    a = 0
    b = 1  # ✅ INIT: First two Fibonacci numbers

    if (num == 1):
        print(0)        # ✅ FIXED: You used `return 0` earlier which didn’t show any output
        return

    elif (num == 2):
        print(a, b, end=' ')  # ✅ FIXED: Earlier you used `end='7'` or nothing — now it's clean spacing

    else:
        print(0, 1, end=' ')  # ❌ You hardcoded 0 and 1 here — better to use `print(a, b, end=' ')`
        for i in range(2, num):  # ✅ FIXED: You were doing `for num in range(...)` — overwrote your input
            c = a + b
            print(c, end=' ')    # ✅ FIXED: Previously printed `c` twice or forgot spacing
            a = b
            b = c

fib(num)  # ✅ FIXED: You had `print(fib(num))` — which printed `None` at the end




# -------------------------------------------------------------
# Program: fibonacci_series.py
# Description: Prints the first N numbers in the Fibonacci series
#
# Key Concepts:
# - if/elif/else
# - for loop
# - variable swapping
# - function with no return, only print
# - handling edge cases: n = 1 and n = 2
#
# Common Mistakes I Fixed:
# - ❌ Used return instead of print → caused no visible output
# - ❌ Reused input variable `num` in for loop → caused logic bug
# - ❌ Used end='' → caused numbers to print without spaces (01)
# - ❌ Printed c twice in loop → caused double outputs
# - ❌ Used print(fib(...)) → printed `None` at the end
#
# Final Learnings:
# - Use `print()` to show output when return is not needed
# - Always use `end=' '` in print() for clean inline formatting
# - Never reuse input variable names in loops
# - Handle small inputs (n = 1 or 2) separately
# - Don't wrap print-only functions inside another print()
# -------------------------------------------------------------
