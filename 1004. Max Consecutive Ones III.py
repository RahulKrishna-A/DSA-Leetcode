class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones = 0
        zeros = 0
        start = 0
        maxs = 0
        for i in range(len(nums)):
            if nums[i]:
                ones += 1
            else:
                zeros += 1
            while zeros > k:
                if nums[start]:
                    ones -= 1
                else:
                    zeros -= 1
                start += 1
            if i - start + 1 > maxs:
                maxs = i - start + 1
        return maxs

