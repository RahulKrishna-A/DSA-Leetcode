class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {}
        for i in range(len(nums)):
            targ = target - nums[i]
            if targ in hashs:
                return [i, hashs[targ]]
            else:
                hashs[nums[i]] = i




