class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = nums[0]
        sums=0
        for i in nums:
            sums+=i
            maxs = max(maxs,sums)
            if sums<0:
                sums=0
        return maxs

