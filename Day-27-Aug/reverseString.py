text = input("Enter the string you want to reverse: ")



def reverseString(text):

    reverseValue = ''

    for char in text:

        reverseValue = char + reverseValue


    return reverseValue


print (reverseString(text))