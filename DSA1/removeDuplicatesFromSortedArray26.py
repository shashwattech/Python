nums = [0,0,1,1,1,2,2,3,3,4]


# def removeDuplicates(nums):


#     for i in nums:

#         for j in nums:

#             if nums[i] == nums[j]:

#                 del nums[j]


    
#     return nums


# print (removeDuplicates(nums))



def removeDuplicates(nums):


    for i in nums:

        if nums[i] == nums[i+1]:

            del nums[i+1]


    
    return nums


print (removeDuplicates(nums))



#LEETCODE ACEEPTED


# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         i=0
#         while i < len(nums) - 1:

#             if nums[i] == nums[i+1]:

#                 del nums[i+1]

#             else: 

#                 i = i+1


    
#         return len(nums)
