class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest=0
        sets = set()
        for i in nums:
            sets.add(i)
        for i in sets:
            if i-1 not in sets:
                cnt =1
                while i+1 in sets:
                    cnt+=1
                    i+=1
                longest = max(cnt,longest)
        return longest


