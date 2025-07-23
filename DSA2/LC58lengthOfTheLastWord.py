s = "Hello World"


def lengthLastWord(s):


    # counter = 0 
    # i = len(s) -1

    # for char in range(len(s), 1):

    #     if s[char] == " ":

    #         pass

    #     else:
    #         while s[char]!= " ":

    #             counter += 1



    # return counter

    i = len(s) -1 
    count = 0

    while i>=0 and  s[i] == " ":

        i = i-1

    while i>=0 and  s[i] != " ":

        count += 1
        i -= 1


    return count





print(lengthLastWord(s))




