text = input("Enter the string in which you want to count vowels: ")




def numberOfVowels(text):
    vowels= "aeiouAEIOUC"

    vowelCount = 0

    for char in text:
        if char in vowels:
            vowelCount = vowelCount + 1

    return vowelCount

print(numberOfVowels(text))