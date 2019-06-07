### This is the Divide-and-Conquer implementation of the 
### Merge Sort algorithm

### Here is the "PseudoCode Description":

### Input : Array A of n distinct numbers
### Output: array with the same integers, sorted from smallest to largest
### ignoring base cases
### C : Recursively sort first half of A
### D : Recursively sort second half of A
### return Merge(C,D)

import numpy as np

size = 25

np.random.seed(130)
A = np.random.randint(low = 10*size, size = size)
print(A)

def MergeAscending(array1, array2):

    i = 0
    j = 0
    n = len(array1) + len(array2)
    B = np.empty(len(array1)+len(array2))

    for k in range(n):

        if array1[i] < array2[j]:

            B[k] = array1[i]
            i = i + 1
            if i == len(array1):
                B[k+1:] = array2[j:]
                break
        else:
            B[k] = array2[j]
            j = j + 1
            if j == len(array2):
                B[k+1:] = array1[i:]
                break    
    return B

def MergeDescending(array1, array2):
    
    i = 0
    j = 0
    n = len(array1) + len(array2)
    B = np.empty(len(array1)+len(array2))

    for k in range(n):

        if array1[i] > array2[j]:

            B[k] = array1[i]
            i = i + 1
            if i == len(array1):
                B[k+1:] = array2[j:]
                break
        else:
            B[k] = array2[j]
            j = j + 1
            if j == len(array2):
                B[k+1:] = array1[i:]
                break    
    return B

# print(Merge(np.array([1,3,5,7,19]),np.array([2,4,6,8,11,12,13,14,15])))

def MergeSort(array, ascending):



    if len(array) <= 1:
        return array
    
    else:
        n = len(array)
        C = array[ : n//2]
        D = array[n//2 :]

        C = MergeSort(C,ascending)
        D = MergeSort(D,ascending)

        if ascending:
            return MergeAscending(C,D)
        else:
            return MergeDescending(C,D)
        
print(MergeSort(array=A,ascending = True))
