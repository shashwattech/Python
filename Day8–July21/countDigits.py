x = int(input("Enter the number you want to count digits for: "))


def countDigits(x):

    x = abs(x)

    x = str(x)

    digits = 0

    for digit in x:

        digits = digits +1 


    
    return digits



print(countDigits(x))