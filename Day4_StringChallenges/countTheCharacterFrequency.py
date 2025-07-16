s = input("Enter the string for counting the character frequency for: " )


def countFrequencyOfCharacter(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] = char_count[char] + 1

        else:
            char_count[char] = 1

    return char_count


print(countFrequencyOfCharacter(s))


# check what is this 

# char_count[char] = char_count.get(char, 0) + 1

# and this char_count[char] += 1


