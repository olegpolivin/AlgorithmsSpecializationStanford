import numpy as np
rand_array = np.random.randint(0,100,size = 10)

def MergeInversionCount(arrayA, arrayB):

    len_a = len(arrayA)
    len_b = len(arrayB)

    n = len_a + len_b
    k = 0
    j = 0
    numInversions = 0
    sortedArray = np.empty(n)
    
    for i in range(n):

        if arrayA[k]<arrayB[j]:
            sortedArray[i] = arrayA[k]
            k = k+1
                
            if k == len_a:
                sortedArray[i+1:] = arrayB[j:]
                break

        else:
            sortedArray[i] = arrayB[j]            
            j = j + 1
            numInversions = numInversions + len_a - k

            if j == len_b:
                sortedArray[i+1:] = arrayA[k:]
                break

    return sortedArray,numInversions

def MergeSortInversionCount(array):

    n = len(array)

    if n < 2:
    
        return array,0
    
    else:

        left, numInversionsLeft = MergeSortInversionCount(array[0:n//2])
        right, numInversionsRight = MergeSortInversionCount(array[n//2:])
        result = MergeInversionCount(left,right)
        return result[0],result[1]+numInversionsLeft+numInversionsRight
    
# print(rand_array)
# print(MergeSortInversionCount(rand_array))


array_from_coursera = open("IntegerArray.txt", "r").readlines()
array_from_coursera_int = [int(t) for t in array_from_coursera]

#print(MergeSortInversionCount([6,5,4,3,2,1])[1])
print(MergeSortInversionCount(array_from_coursera_int)[1])