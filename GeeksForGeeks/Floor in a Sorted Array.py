class Solution:
    # User function Template for python3

    # Complete this function
    def findFloor(self, A, N, X):
        # Your code here
        if A[0] >= X:
            return -1

        l = 0
        h = N - 1
        while l <= h:
            mid = l + (h - l) // 2
            if A[mid] > X:
                h = mid - 1
            else:
                l = mid + 1
        return h

