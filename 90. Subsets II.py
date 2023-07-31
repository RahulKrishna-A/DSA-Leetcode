class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = 0
        s = 0
        old_nums = [[]]
        nums.sort()
        for i in range(len(nums)):
            s = 0
            if i != 0 and nums[i] == nums[i - 1]:
                s = l + 1
            l = len(old_nums) - 1
            new_nums = []
            for j in range(s, l + 1):
                new_nums.append(old_nums[j] + [nums[i]])
            old_nums += new_nums
        return old_nums

