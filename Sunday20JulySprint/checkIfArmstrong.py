
x = int(input("Enter the nmber which you want to check is integer or not: "))


def checkArmstrong(x):

    
    x = str(x)

    y = len(x)

    sum = 0

    for i  in x:

        sum = sum  + (int(i) ** y) # here you didnt change the typr to int while evaluating 

    return sum



if (checkArmstrong(x) == x):

    print("True") 

else:

    print("False") 




