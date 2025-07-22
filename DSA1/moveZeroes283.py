nums = [0,1,0,3,12]


def moveZeroes(nums):

    a =[]
    b =[]


    for i in nums:

        if (i == 0):

            a.append(i)
        
        else:

            b.append(i)


    finalList = b+a

    # for i in range(len(nums)):
    #         nums[i] = finalList[i]. ##your solution wasnt accepted w/o this since you dont have to return a new list but overwrite the same list


    return finalList



print(moveZeroes(nums))





#LEETCODE VERSION


# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """

#         a =[]
#         b =[]


#         for i in nums:

#             if (i == 0):

#                 a.append(i)
            
#             else:

#                 b.append(i)


#         finalList = b+a

#         for i in range(len(nums)):
#             nums[i] = finalList[i]

    
#         return nums