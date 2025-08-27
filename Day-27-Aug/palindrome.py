text = input("Enter the string you eant to check is palindrome: ")



def checkPalindrome(text):


    reverseText = ''

    for char in text:

        reverseText = char + reverseText

    
    if (text == reverseText):

        return True
    
    else:

        return False
    


print (checkPalindrome(text))