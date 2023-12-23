class Solution:
    def solve(self, n, k, stalls):

        def canPlace(dist):
            totcow = 1
            last = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last >= dist:
                    totcow += 1
                    last = stalls[i]
                if totcow >= k:
                    return True
            return False

        stalls.sort()
        s = 0
        e = stalls[n - 1] - stalls[0]
        ans = 0

        while s <= e:
            mid = s + (e - s) // 2

            if canPlace(mid):
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
        return ans
