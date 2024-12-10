'''
Dylan Davis
3047302
EECS 330
11/20/23
sorting algorithms 
'''

from random import randint, seed
import time

class Sorting:
    def __init__(self, size):
        self.arr = []  
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

    def selection_sort(self):
        """Implements selection sort"""
        for i in range(len(self.arr)):  
            minIndex = i 
            for j in range(i + 1, len(self.arr)): 
                if self.arr[j] < self.arr[minIndex]:  
                    minIndex = j 
            self.arr[i], self.arr[minIndex] = self.arr[minIndex], self.arr[i] 

    def max_heapify(self, n, i):
        """Implements Heapify for array"""
        biggestNode = i  
        leftChild = 2 * i + 1 
        rightChild = 2 * i + 2 

        if leftChild < n and self.arr[leftChild] > self.arr[biggestNode]:  
            biggestNode = leftChild 

        if rightChild < n and self.arr[rightChild] > self.arr[biggestNode]:  
            biggestNode = rightChild 
        if biggestNode != i:
            self.arr[i], self.arr[biggestNode] = self.arr[biggestNode], self.arr[i] 
            self.max_heapify(n, biggestNode)  

    def heap_sort(self):
        """Implements Heap sort"""
        for i in range((len(self.arr)) // 2 - 1, -1, -1):  
            self.max_heapify((len(self.arr)), i)  
        for i in range((len(self.arr)) - 1, 0, -1): 
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]  
            self.max_heapify(i, 0) 

    def merge_sort(self):
        """Implements Merge sort"""
        def merge(left, right):  
            mergedArray = []  
            leftIndex = 0 
            rightIndex = 0 

            while leftIndex < len(left) and rightIndex < len(right): 
                if left[leftIndex] < right[rightIndex]:  
                    mergedArray.append(left[leftIndex])  
                    leftIndex += 1 
                else:  
                    mergedArray.append(right[rightIndex]) 
                    rightIndex += 1 

            mergedArray.extend(left[leftIndex:]) 
            mergedArray.extend(right[rightIndex:]) 
            self.arr[:] = mergedArray  

        if len(self.arr) <= 1: 
            return 

        middle = len(self.arr) // 2  
        leftHalf = self.arr[:middle] 
        rightHalf = self.arr[middle:] 

         
        self.arr = leftHalf 
        self.merge_sort()  
        leftSorted = self.arr 
        
        self.arr = rightHalf 
        self.merge_sort()  
        rightSorted = self.arr  

        merge(leftSorted, rightSorted) 

    def test_sorting_time(self, sorting_method):
        startTime = time.time()
        if sorting_method == 'selection':
            self.selection_sort()
        elif sorting_method == 'heap':
            self.heap_sort()
        elif sorting_method == 'merge':
            self.merge_sort()
        end_time = time.time()
        return end_time - startTime


# Test Sorted array
def is_sorted(arr):
    if arr == sorted(arr):
        return "Passed!"
    else:
        return "Failed!"

# Test each sorting technique
def test_sort_algorithms(sorting_method, set_seed=None):
    if set_seed is not None:
        seed(set_seed)
    sorting = Sorting(10)
    # Add 10 random elements
    for _ in range(10):
        sorting.add(randint(1, 100))
    # Apply the sorting algorithm
    if sorting_method == 'selection':
        sorting.selection_sort()
        print("Selection Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'heap':
        sorting.heap_sort()
        print("Heap Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'merge':
        sorting.merge_sort()
        print("Merge Sort:", is_sorted(sorting.arr))

# Test run time
def run_time_tests():
    seeding = 45
    array_sizes = [10000, 20000, 30000, 40000, 50000]
    methods = ['selection', 'heap', 'merge']
    print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
    for size in array_sizes:
        times = []
        for m in methods:
            sorting = Sorting(size)
            seed(seeding)
            for _ in range(size):
                sorting.add(randint(1, 50000))
            interval = sorting.test_sorting_time(m)
            times.append(interval)
        print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")

# Test case execution
seed_num = 43
test_sort_algorithms('selection', seed_num)
test_sort_algorithms('heap', seed_num)
test_sort_algorithms('merge', seed_num)
run_time_tests()

'''
Selection Sort:
The Time complexity for selection sort is O(n^2).
Selection Sort uses nested loops to iterate through an array until it is completely sorted
As N gets bigger so to does the run time, it takes for Selection Sort longer an longer given large n
This is the least efficient algorithm, bad for large number of n. 

Heap Sort:
The time complexity for Heap Sort is O(n log n),
Heap sort a builds max heap and then repeatedly extracts the root while maintaining a heaps properties
Heao sort works well for large inputs of n. 

Merge Sort:
The time complexity for merge sort is also O(n log n)
merge sort divides an array into halves, it then sorts them, and merges the two sorted halves together
Merging into itself has a time complexity of linear O(n).
Performs well for large inputs of n like Heap sort, and the time complexity is the same.
Merge sort is the most efficient algorithm for most scenarios.
'''