x = int(input("Enter the number for which you want the sum of digits: "))


def sumOfDigits(x):

    x = abs(x)

    x = str(x)


    sum = 0


    for i in x:

        sum = sum + int(i)


    return sum


print(sumOfDigits(x))