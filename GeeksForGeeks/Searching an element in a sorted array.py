#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        l=0
        r=N-1
        while l<=r:
            mid = l + (r-l)//2
            if arr[mid]==K:
                return 1
            elif arr[mid]>=K:
                r=mid-1
            else:
                l=mid+1
        return -1

