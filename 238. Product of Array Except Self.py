class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            out[i] = pre
            pre *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            out[j] *= post
            post *= nums[j]
        print(out)
        return out
