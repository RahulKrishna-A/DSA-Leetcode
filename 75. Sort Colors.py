class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        start = 0
        for i in counts:
            for j in range(counts[i]):
                nums[start] = i
                start += 1


