checkin = input("Enter the string you ant to count vowel for: ")

def countVowels(checkin):

    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count =0

    for char in checkin:

        if char in vowels:

            count += 1


    return count



print(countVowels(checkin))

