'''
Author : Harshita Sharma
Date :  10/31/2019
'''

'''
BubbleSort:
Traverse an array A from left till you find, A[i] > A[i+1], then swap and i++, 
In the same pass keep swapping till max(A) reaches at the last index of array.

Continue next passes but now till n-1, where n= number of elements.
'''

def bubble_sort(A,n):
    for k in range(0,n-1):
        swap_happened = False
        for i in range(0,n-k-1):
            if(A[i]>A[i+1]):
                #Swap adjascent numbers..
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                swap_happened = True
        if swap_happened == False :
            ## Here, iF no two elements were swapped, then break the loop
            ## Array is sorted now!!
            break
    return A

if __name__ =='__main__':
    A = list(map(int,input().split()))
    A_sorted = bubble_sort(A,len(A))
    print(*A_sorted)


