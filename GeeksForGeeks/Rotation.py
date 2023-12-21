# User function Template for python3
class Solution:
    def findKRotation(self, arr, n):
        # code here
        s = 0
        e = n - 1
        while s <= e:
            mid = s + (e - s) // 2
            if mid > s and arr[mid] < arr[mid - 1]:
                return mid
            elif mid < e and arr[mid] > arr[mid + 1]:
                return mid + 1
            elif arr[mid] >= arr[s]:
                s = mid + 1
            else:
                e = mid - 1
        return 0
