x = int(input("Enter the number you want the factorial for: "))

def factorial(x):

    factorial = 1

    for i in range(2, x+1):

        factorial = factorial * i


    
    return factorial



print(factorial(x))