class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        ind = []
        print(counts)
        for i in counts:
            if counts[i] > len(nums) / 3:
                ind.append(i)

        return ind

