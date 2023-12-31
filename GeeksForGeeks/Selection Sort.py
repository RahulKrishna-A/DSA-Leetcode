# User function Template for python3

class Solution:
    def select(self, arr, i):
        # code here
        minimum = i
        for i in range(i, len(arr)):
            if arr[minimum] > arr[i]:
                minimum = i
        return minimum

    def selectionSort(self, arr, n):
        # code here
        for i in range(n):
            min_index = self.select(arr, i)
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr
