input1 = input("Enter the first word for checking if anagram: ")
input2 = input("Enter the second word for checking if anagram: ")


def checkTheFrequencyofCharacter (input):

    frequency_map = {}

    for char in input:

        if char in frequency_map:

            frequency_map[char] = frequency_map[char] + 1

        else:

            frequency_map[char] = 1


    return frequency_map


if (checkTheFrequencyofCharacter(input1) == checkTheFrequencyofCharacter(input2)):
    print (True, "They are Anagram")
else:
    print(False, "They are not anagram")


# Renamed checkTheFrequencyofCharacter to getCharFrequencyMap — this is more accurate.

# Used += 1 instead of = frequency_map[char] + 1 (both are fine, but += is cleaner).

# Added spacing and formatting for clarity.

# You're returning two values in print(False, "They are not anagram") — which is okay, but consider just printing the message if you're not using the Boolean result anywhere.