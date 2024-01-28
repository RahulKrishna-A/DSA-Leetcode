class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def getatmostk(s):
            maps = {}
            start = 0
            ans = 0
            for i in range(len(nums)):
                maps[nums[i]] = maps.get(nums[i], 0) + 1
                while len(maps) > s:
                    if maps[nums[start]] == 1:
                        del maps[nums[start]]
                    else:
                        maps[nums[start]] -= 1
                    start += 1
                ans += (i - start + 1)
            return ans

        return getatmostk(k) - getatmostk(k - 1)


