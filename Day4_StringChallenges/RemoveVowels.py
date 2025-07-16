s= input("Enter the string you want to remove vowels from:" )


def removeVowels(s):
    result = ''
    vowels = "aeiouAEIOU"

    for char in s:
        if char not in vowels:

            result =result + char  

    return result


print(removeVowels(s))
