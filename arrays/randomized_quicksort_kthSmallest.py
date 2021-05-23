import random

def main ():
    arr = [12, 3, 5, 7, 4, 19, 26]
    val = kthsmallest(arr, 0, len(arr)-1, 3)
    print (val)

def kthsmallest(arr, l, r, k):
    if (k>0 and k<=r-l+1):      
        pos = rand_partition(arr, l, r)
        if (pos - l == k-1):
            return arr[pos]
        if (pos -l < k -1):
            return kthsmallest(arr, pos+1, r, k - (pos - l+1))   # k - num of elements to the left including pos element.
        return kthsmallest(arr, l, pos-1, k)     
    return 999999999

def rand_partition(arr, l, r):
    x = arr[r]
    rand_ind = random.randint(l,r)
    arr[r], arr[rand_ind] = arr[rand_ind], arr[r]
    return partition(arr, l, r)

def partition (arr, l, r):
    x = arr[r]
    i=l
    # i points to the greater than x elements and j goes on to find smaller than x elements. Once found they swap.
    for j in range(l, r):
        if (arr[j]<=x):
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[r] = arr[r], arr[i]
    return i












if (__name__ == '__main__'):
    main()
