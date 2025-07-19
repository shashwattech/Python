num = int(input("Enter the number you want the factorial for: "))


def factorial(num):

    if (num == 0 or num == 1):

        return 1
    
    factorial = 1
    
    for i in range(2, num+1): #revise why did you use n +1 and not n ---> whwn you wrote yourself you wrote n

        factorial = factorial * i



    return factorial


print (factorial(num))
