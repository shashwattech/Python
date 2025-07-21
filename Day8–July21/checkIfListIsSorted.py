list1 = [1, 2, 3, 4, 5]
list2 = [3,2,1]


def checkSorted(list1):

    for elements in range(len(list1) - 1):

        if (list1[elements] > list1[elements+1]):


            return False
        
        else :

            return True
        
print(checkSorted(list2))
print(checkSorted(list1))