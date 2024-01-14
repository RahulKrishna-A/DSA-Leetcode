# User function Template for python3
class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        # code here
        sums = 0
        maxs = 0
        for i in range(K):
            sums += Arr[i]
        j = K
        i = 0
        maxs = sums
        while j <= N - 1:
            sums += Arr[j]
            sums -= Arr[i]
            j += 1
            i += 1
            maxs = max(maxs, sums)
        return maxs


