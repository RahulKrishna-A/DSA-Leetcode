class Solution:
    def sort012(self, arr, n):
        # code here
        low, mid, high = 0, 0, len(arr) - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr
