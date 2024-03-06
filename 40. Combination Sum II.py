class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        cand.sort()
        res = []

        def helper(ind, target, ans):
            if target == 0:
                res.append(ans[:])
                return
            if ind == len(cand):
                return

            for i in range(ind, len(cand)):
                if i > ind and cand[i] == cand[i - 1]:
                    continue
                if cand[i] > target:
                    break
                ans.append(cand[i])
                helper(i + 1, target - cand[i], ans)
                ans.pop()

        helper(0, target, [])
        return res
