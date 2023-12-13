class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        brk_pnt = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                brk_pnt = i
                break
        if brk_pnt == -1:
            i = 0
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums
        for i in range(len(nums) - 1, brk_pnt, -1):
            if nums[i] > nums[brk_pnt]:
                nums[i], nums[brk_pnt] = nums[brk_pnt], nums[i]
                break
        i = brk_pnt + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums


