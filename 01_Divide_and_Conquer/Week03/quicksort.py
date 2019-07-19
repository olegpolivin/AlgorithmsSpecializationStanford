f = open("QuickSort.txt", "r")
A = f.readlines()
A = [int(i) for i in A]

# A = [6, 1, 5, 8, 3, 2, 10, 10, 2, 4, 7, 8, 4]

def Partition(A, l, r):

    """
    Partition subroutine: partition the array around pivot
    l, r = left and right endpoints 
    """

    p = A[l] #Pivot point, first element because we put it there in the QS algorithm
    i = l+1
    
    for j in range(l+1, r+1):

        if A[j] < p :
  
            A[i], A[j] = A[j], A[i] # Swap the two elements
            i = i + 1
        
    # Swap pivot and the last element that is lower than pivot
    A[l], A[i-1] = A[i-1], p

    return i-1 #Report poisition of the pivot element

def ChoosePivot(A,l,r):

    """
    Choose pivot subroutine. 
    For Coursera's Assignment it will be a particular simplified one
    """
    # pivot_index  = l # First element
    # pivot_index  = r # Last element

    middle = l+(r-l)//2

    a1 = A[l]
    a2 = A[r]
    a3 = A[middle]


    if (a2<=a3)&(a2>=a1):
        pivot_index = r
    elif (a3<=a2)&(a3>=a1):
        pivot_index = middle
    elif (a1<=a3)&(a1>=a2):
        pivot_index = l
    elif (a3<=a1)&(a3>=a2):
        pivot_index = middle
    elif (a1<=a2)&(a1>=a3):
        pivot_index = l
    elif (a2<=a1)&(a2>=a3):
        pivot_index = r
    else:
        raise Exception
    
    return pivot_index

def QS(A,l,r,lst=[]):
    """
    Implementation of the QuickSort Algorithm with simplified ChoosePivot routine
    l, r = left and right end points
    """

    if l >= r:
        
        return #Base case
    
    else:
        lst.append(r-l)
        i = ChoosePivot(A,l,r)
        A[l], A[i] = A[i], A[l] # Put pivot element first
        j = Partition(A,l,r) # New pivot position

        QS(A,l,j-1,lst) #Recurse on first part
        QS(A,j+1,r,lst) #Recurse on second part
        
        return sum(lst)


n = len(A) - 1
# print(A)
print(QS(A,0,n,lst=[]))
# print(A)
