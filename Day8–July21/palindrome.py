x = int(input("Enter the number you want to check ids palindrome: "))

def isPalindrome(x):

    x = str(x)

    reversedNumber = ""

    for i in x:

        reversedNumber = i + reversedNumber


    if int(x) == int(reversedNumber):

        return True
    else:

        return False


print (isPalindrome(x))
