# User function Template for python3

class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Complete the function
        memo = {}
        max_sums = 0
        sums = 0
        for i in range(n):
            sums += arr[i]
            if sums == k:
                max_sums = max(i + 1, max_sums)
            if sums - k in memo:
                max_sums = max(i - memo[sums - k], max_sums)
            if sums not in memo:
                memo[sums] = i

        return max_sums
