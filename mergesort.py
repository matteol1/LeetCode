def mergeSort(array):
    if len(array)==1 or len(array)==0:
        return array
    left_array = mergeSort(array[0:len(array)//2])
    right_array = mergeSort(array[len(array)//2 : len(array)])
    #splitting O(log n)
    i, j = 0, 0
    sorted_array = []
    #print(f"Left: {left_array}")
    #print(f"Right: {right_array}")

    #merging back O(n) 2 indices running over the two pieces 
    while i < len(left_array) and j < len(right_array):
        if left_array[i]<right_array[j]:
            sorted_array.append(left_array[i])
            i+=1
        else:
            sorted_array.append(right_array[j])
            j+=1
    #at this point either left or right array still may have elements to add, but they are already sorted
    if i == len(left_array) and j == len(right_array):
        return sorted_array
    elif i == len(left_array):
        #sorted_array.append(right_array[j:len(right_array)-1]) 
        for k in range(j,len(right_array)):
            sorted_array.append(right_array[k])
        return sorted_array
    else:
        #sorted_array.append(left_array[i:len(left_array)-1]) 
        for k in range(i,len(left_array)):
            sorted_array.append(left_array[k])
        return sorted_array

test_array = [1,2,0,1,1,2,4,5,6,7,2,4,5,2,7,2,4,6,2,3,4,1,2,3,4]
#print(test_array[0:len(test_array)//2])
#print(test_array[len(test_array)//2 : len(test_array)])
#
#test_array2 = [0,0]
#print(test_array2[0:len(test_array2)//2])
#print(test_array2[len(test_array2)//2 : len(test_array2)])

print(mergeSort(test_array))