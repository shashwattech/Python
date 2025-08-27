numbers = [2, 8, 1, 6, 3]


def findMax(numbers):
    maximum = numbers[0] 
    for num in numbers:

        if (num > maximum):

            maximum = num

    return maximum


print (findMax(numbers))

