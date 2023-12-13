class Solution:
    def trappingWater(self, arr, n):
        # Code here
        maxleft = 0
        maxright = 0
        l = 0
        r = n - 1
        res = 0
        while l <= r:
            if arr[l] <= arr[r]:
                if arr[l] > maxleft:
                    maxleft = arr[l]
                else:
                    res += maxleft - arr[l]
                l += 1
            else:
                if arr[r] > maxright:
                    maxright = arr[r]
                else:
                    res += maxright - arr[r]
                r -= 1
        return res
