class Solution:
    def insert(self, alist, index, n):
        # code here
        pass

    # Function to sort the list using insertion sort algorithm.
    def insertionSort(self, arr, n):
        # code here
        for i in range(n):
            j = i
            while (j > 0 and arr[j] < arr[j - 1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        return arr