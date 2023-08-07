class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        maxs=0
        ind = -1
        print(counts)
        for i in counts:
            if counts[i]>maxs:
                ind = i
                maxs = counts[i]
        return ind

