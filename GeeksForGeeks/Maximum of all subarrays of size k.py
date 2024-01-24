# User function Template for python3
from collections import deque


class Solution:

    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):

        # code here
        q = deque()
        ans = []
        for i in range(n):
            while q and arr[q[-1]] <= arr[i]:
                q.pop()
            q.append(i)

            while q and q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                ans.append(arr[q[0]])
        return ans
