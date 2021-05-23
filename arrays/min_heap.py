# This shows the custom and library implementation of min heap.
# min heap and max heap are represented as arrays.
# arr[0] -> root element; arr[2*i-1] left element and arr[2*i+1] right element; arr[(i-1)/2] parent element.
# Operations on the min heap
    # getMin(): O(1)
    # extractMin(): O(logn)
    # decreaseKey(): O(logn)
    # insert(): O(logn)
    # delete(): O(logn): first decreaseKey (with -INT_INF) is applied on the node and then extractMin() is applied.

# below class MinHeap implements the python library version of min heap.
from heapq import heappush, heappop, heapify

class MinHeapLib:
    def __init__(self):
        self.heap = []
    
    def insertKey(self, k):
        heappush(self.heap, k)
    
    def parent (self, i):
        return int ((i-1)/2)
    
    def getMin(self):
        return self.heap[0]
    
    def extractMin(self):
        return heappop(self.heap)
    
    def decreaseKey(self, i , k):
        if (k < self.heap[i]):
            # this updates upwards
            self.heap[i] = k
            while (i!=0 and self.heap[self.parent(i)] > self.heap[i]):
                # swap parent and current
                self.heap[self.parent(i)] , self.heap[i] = self. heap[i], self.heap[self.parent(i)] 
        else:
            # this updates downwards
            pass
            # TODO

    def deleteKey(self, i):
        self.decreaseKey(i, -999999)
        self.extractMin()







def main():
    # using library
    heapObj = MinHeapLib()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    heapObj.deleteKey(1)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.insertKey(45)
    
    print (heapObj.extractMin())
    print (heapObj.getMin())
    heapObj.decreaseKey(2, 1)
    print (heapObj.getMin())


    # using custom implementation



if (__name__ == "__main__"):
    main()
