listToFindMax = [12,234,543,764,654,76654,8653,75438,37654,73547904654,763443]

max_num = -1
for nums in listToFindMax:

    if nums > max_num:
        max_num = nums
# while checking the comparison value, check with repect to iterator value

print("The largest number in the list is: ", max_num)
