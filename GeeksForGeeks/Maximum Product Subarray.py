# User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr, n):
        # code here
        pre = 1
        suf = 1
        maxis = - float("inf")
        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre *= arr[i]
            suf *= arr[n - i - 1]
            maxis = max(maxis, max(pre, suf))

    return maxis
