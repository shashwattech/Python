Alist = [2,3,45,68,87,98,87,68,54,34,67,6,0]

def sumOfEvenNumbersInAList(Alist):

    sum = 0

    for num in Alist:
        if num%2 == 0:

            sum = sum + num


    return sum

print(sumOfEvenNumbersInAList(Alist))

