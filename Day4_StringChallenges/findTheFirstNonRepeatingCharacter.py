s = input("Enter the string which you want to check first non repeating charracter for: ")


def recordFrequency(s):

    frequency_counter = {}

    for char in s:

        if char in frequency_counter:

            frequency_counter[char] = frequency_counter[char] + 1

        else:

            frequency_counter[char] = 1

    return frequency_counter


print (s)
for char, count in recordFrequency(s).items():

    if count == 1:
        print("The character with single frequency is: ", char)
        break
