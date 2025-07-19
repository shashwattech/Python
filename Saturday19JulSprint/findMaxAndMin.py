Input=  [3, 5, 1, 8, 2]

def findMaxMin(Input):

    min = Input[0]

    max= Input[0]


    for i in Input:

        if i > max:

            max = i

        elif i<min:

            min = i

    
    return [max, min]
    

print(findMaxMin(Input))



# Input = [3, 5, 1, 8, 2]  # ✅ Sample input list to test max–min logic

# def findMaxMin(Input):

#     min = Input[0]  # ✅ Initialize min to the first element of the list
#     max = Input[0]  # ✅ Initialize max to the first element of the list

#     for i in Input:  # ✅ Loop through each element in the list

#         if i > max:
#             max = i  # ✅ Update max if current value is greater

#         elif i < min:
#             min = i  # ✅ Update min if current value is smaller

#     return [max, min]  # ✅ Return the final max and min values

# print(findMaxMin(Input))  # ✅ Call the function and print result: Output → [8, 1]







# # ✅ Sample input list to test max–min logic
# Input = [3, 5, 1, 8, 2]

# def findMaxMin(Input):

#     # 🔹 Always initialize min and max with the first element of the list
#     #    This ensures that the comparisons work correctly even with negatives
#     min = Input[0]
#     max = Input[0]

#     # 🔹 Loop through each number in the list to compare and update min/max
#     for i in Input:

#         # 🔹 If current number is greater than max, update max
#         if i > max:
#             max = i

#         # 🔹 If current number is smaller than min, update min
#         elif i < min:
#             min = i

#     # 🔹 Do NOT return inside the loop — wait until all comparisons are done
#     return [max, min]

# # 🔹 Function call to display result
# #    Expected Output: [8, 1] → 8 is the max, 1 is the min
# print(findMaxMin(Input))



# ❌ DO NOT initialize max or min to 0 — use the first element of the list
# ❌ DO NOT return inside the loop — it exits too early
# ❌ Avoid using built-in names like `min` and `max` as variable names in large projects
# ✅ Loop fully, compare properly, and return final result after loop ends
