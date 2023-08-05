class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        poss = []
        self.newComb(candidates, target, ret, poss)
        return ret

    def newComb(self, arr, target, ret, poss):
        if target == 0:
            ret.append(poss[:])
            return
        for i in arr:
            if i <= target:
                poss.append(i)
                self.newComb(arr[:], target - i, ret, poss)
                poss.pop()
                arr = arr[1:]

