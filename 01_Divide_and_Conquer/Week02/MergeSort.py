import numpy as np
rand_array = np.random.randint(0,100,size = 10)

def Merge(arrayA, arrayB, ascending = True):

    len_a = len(arrayA)
    len_b = len(arrayB)

    n = len_a + len_b
    k = 0
    j = 0
    sortedArray = np.empty(n)
    
    if ascending:

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

                if j == len_b:
                    sortedArray[i+1:] = arrayA[k:]
                    break
    else:

        for i in range(n):

            if arrayA[k]>arrayB[j]:
                sortedArray[i] = arrayA[k]
                k = k+1
                
                if k == len_a:
                    sortedArray[i+1:] = arrayB[j:]
                    break

            else:
                sortedArray[i] = arrayB[j]            
                j = j + 1

                if j == len_b:
                    sortedArray[i+1:] = arrayA[k:]
                    break
    
    return sortedArray


def MergeSort(array, ascending = True):

    n = len(array)

    if n < 2:
        return array
    
    else:
        left = MergeSort(array[0:n//2],ascending = ascending)
        right = MergeSort(array[n//2:], ascending = ascending)

        return Merge(left,right, ascending = ascending)

print(rand_array)
print(MergeSort(rand_array,ascending = False))


    