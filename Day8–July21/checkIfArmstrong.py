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



