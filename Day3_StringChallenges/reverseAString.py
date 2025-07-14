def reverseAString(text):

    newText = ""
    for char in text:

        newText = char + newText 


    return newText



text = str(input("Enter the text to be reversed: " ))

print (reverseAString(text))