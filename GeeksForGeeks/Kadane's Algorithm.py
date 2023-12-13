# User function Template for python3

class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        ##Your code here
        max_sum = arr[0]
        sums = 0
        for i in range(0, N):
            sums += arr[i]
            max_sum = max(sums, max_sum)
            if sums < 0:
                sums = 0

        return max_sum
