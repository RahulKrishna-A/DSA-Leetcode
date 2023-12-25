class Solution:
    def splitArray(self, arr, N, K):
        # code here
        def canSum(target):
            arrs = 1
            arr_sum = 0
            for i in range(N):
                if arr_sum + arr[i] <= target:
                    arr_sum += arr[i]
                else:
                    arr_sum = arr[i]
                    arrs += 1
            return arrs

        s = max(arr)
        e = sum(arr)
        ans = 0
        while s <= e:
            mid = s + (e - s) // 2
            # prin

            if canSum(mid) > K:
                s = mid + 1
            else:
                e = mid - 1
        return s
