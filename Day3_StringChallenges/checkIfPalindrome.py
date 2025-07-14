stringToCheck = input("Enter the string to be checked: ")


def checkPalindrome(stringToCheck):

    reversedString = ""

    for char in stringToCheck:

        reversedString = char + reversedString


    return reversedString


if stringToCheck  == checkPalindrome(stringToCheck):
    print("Yes its a palindrom")
else:
    print("Not a palindrome")


#here is the slicing version:

# stringToCheck = input("Enter the string to be checked: ")

# if stringToCheck == stringToCheck[::-1]:
#     print("Yes, it's a palindrome")
# else:
#     print("Not a palindrome")


