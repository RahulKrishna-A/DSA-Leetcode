class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for i in nums:
            if i in s:
                return True
            else:
                s[i] = 1

        return False
