array = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray(array):
    maxSub = array[0]
    curSum = 0

    for i in array:

        if curSum < 0:

            curSum = 0

        curSum = curSum + i


        if curSum > maxSub:
            maxSub = curSum



    return maxSub


print (max_subarray(array))









# def max_subarray(array):
#     # Edge case: if the array is empty, return 0 (optional handling)
#     if not array:
#         return 0

#     # maxSub will keep track of the maximum sum found so far
#     maxSub = array[0]

#     # curSum will keep track of the current running subarray sum
#     curSum = 0

#     # Loop through each number in the array
#     for i in array:
#         # If the running sum becomes negative, reset it to 0
#         if curSum < 0:
#             curSum = 0

#         # Add the current element to the running sum
#         curSum += i

#         # Update maxSub if the current running sum is greater than the max found so far
#         maxSub = max(maxSub, curSum)

#     # Return the maximum subarray sum
#     return maxSub







# ✅ Problem:
# Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# 🧠 Approach:
# We use Kadane’s Algorithm, which runs in O(n) time.

# The idea is to accumulate a running sum (curSum), and if it drops below zero, we reset it.

# We track the maximum sum we’ve seen so far using maxSub.

# 🚀 Logic Flow:
# Initialize curSum = 0 and maxSub = array[0].

# Loop through the array:

# If curSum drops below 0, reset it to 0 (because negative sums can't help future subarrays).

# Add current value to curSum.

# Update maxSub to the maximum of itself and curSum.
    
