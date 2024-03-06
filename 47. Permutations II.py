class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def helper(p,up):
            if up==[]:
                if p not in ans:
                    ans.append(p[:])
                return
            for i in range(len(p)+1):
                if i>0 and up[0]==p[i-1]:
                    continue
                helper(p[:i]+[up[0]]+p[i:],up[1:])
        helper([],nums)
        return list(ans)


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        hashx = {}
        for i in nums:
            hashx[i] = hashx.get(i, 0) + 1

            def helper(perm):
                if len(perm) == len(nums):
                    ans.append(perm[:])
                    return

                for i in hashx:
                    if hashx[i] >= 1:
                        perm.append(i)
                        hashx[i] -= 1
                        helper(perm)

                        perm.pop()
                        hashx[i] += 1

            helper(perm)
        return ans
