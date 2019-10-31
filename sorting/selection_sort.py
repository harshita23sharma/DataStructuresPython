'''
Author : Harshita Sharma
Date :  10/31/2019
'''

'''
Selection Sort:
Swapping is done not in between adjascent lements but 
An array A is scanned from starting,look for a minimum element in [0,n) where n is number of elements. If found swap
now again look for next minimum.in [1,n)

So, we are selecting a minimum in each pass and putting in an appropriate position by swapping.
'''

def selection_sort(A,n):
    for k in range(0,n-1):
        k_min = k  ## Initially we can say the starting index in the loop is only minimum..
        for i in range(k+1,n):
            if(A[i] < A[k_min]):
                k_min = i ##update the index of minimum element
        temp = A[k]
        A[k] = A[k_min]
        A[k_min] = temp
    return A

if __name__ =='__main__':
    A = list(map(int,input().split()))
    A_sorted = selection_sort(A,len(A))
    print(*A_sorted)
