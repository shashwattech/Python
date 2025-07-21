Input1 = [3, 5, 1, 8, 2]


Input2 =  [10, 10, 9]


def secondLargest(x):

    largest = 0

    second_largest = 0


    for i in x :

        if (i> largest) :

            second_largest = largest
            largest = i

        elif (i>second_largest and i< largest):

           second_largest = i

    return second_largest


print (secondLargest(Input1))
print (secondLargest(Input2))