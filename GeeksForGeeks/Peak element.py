# your task is to complete this function
# function should return index to the any valid peak element
class Solution:
    def peakElement(self,arr, n):
        # Code here
        s=0
        e=n-1
        while s<e:
            mid=s+(e-s)//2
            if mid<e and arr[mid]>arr[mid+1]:
                e=mid
            else:
                s=mid+1
        return s

