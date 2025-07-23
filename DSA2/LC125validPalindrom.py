
s =[]

def isPalindrome(S):

    def checkPalindrom(s):

        for char in s:

            reversedString = ""


            for char in s:

                if not char.isalnum():

                    pass
                else:

                    reversedString = char + reversedString


        return reversedString


    string  = ""
    for char in s:

        if not char.isalnum():

            pass

        else:

            string = string + char


    if (string == checkPalindrom(s)):

        return (string == checkPalindrom(s))

    else:

        return (string == checkPalindrom(s))





########################LEEET CODE VERSION


# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """


        # def checkPalindrome(s):


        #     reversedString = ""

        #     for char in s:

        #         # if char in [' ', ',', ':', '.','@','#','_']:
        #         #     pass
        #         # if not char.isalpha():
        #         #     pass

        #         if not char.isalnum():
        #             pass

        #         else:
        #             reversedString = char.lower() + reversedString


        #     return reversedString


        # string = ''
        # for char in s:
        #     # if char in [' ', ',', ':','.','@','#','_']:
        #     #     pass
        #     # if not char.isalpha():
        #         #     pass

        #     if not char.isalnum():
        #         pass
        #     else:
        #         string = string + char.lower()
        # if (string == checkPalindrome(s)):
        #     return string == checkPalindrome(s)

        # else:
        #     return string == checkPalindrome(s)






