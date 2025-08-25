nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]    


def mergeSortedArray(nums1, nums2):

    nums3 = []

    i = j = 0

    while i< len(nums1) and  j < len(nums2):

        if nums1[i] <= nums2[j]:

            nums3.append(nums1[i])

            i +=1

        if nums1[i] >= nums2[j]:

            nums3.append(nums2[j])

    while i< len(nums1):

        nums3.append(nums1[i])

    while j < len(nums2):

        nums3.append(nums2[j])

    return nums3



print(mergeSortedArray(nums1, nums2))
        
