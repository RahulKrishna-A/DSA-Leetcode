class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        abs_max = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                abs_max = max(abs_max, count)
                count = 0
            if nums[i] == 1:
                count += 1
        abs_max = max(abs_max, count)
        return abs_max

