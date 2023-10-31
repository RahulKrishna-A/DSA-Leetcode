class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findpivot(arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if mid < r and arr[mid] > arr[mid + 1]:
                    return mid
                if mid > l and arr[mid] < arr[mid - 1]:
                    return mid - 1
                if arr[mid] > arr[l]:
                    l = mid + 1
                elif arr[mid] <= arr[l]:
                    r = mid - 1
            return -1

        def binarysearch(arr, l, r):

            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        pivot = findpivot(nums)
        if pivot == -1:
            return binarysearch(nums, 0, len(nums) - 1)
        else:
            lsearch = binarysearch(nums, 0, pivot)
            if lsearch != -1:
                return lsearch
            else:
                return binarysearch(nums, pivot + 1, len(nums) - 1)







