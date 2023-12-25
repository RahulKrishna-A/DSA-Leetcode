class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMake(max_days):
            flowers = 0
            bouq = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= max_days:
                    flowers += 1
                    if flowers == k:
                        flowers = 0
                        bouq += 1
                else:
                    flowers = 0
            return bouq

        s = min(bloomDay)
        e = max(bloomDay)
        if len(bloomDay) < m * k:
            return -1
        ans = e
        while s <= e:
            mid = s + (e - s) // 2

            if canMake(mid) == m:
                ans = mid
                e = mid - 1
            elif canMake(mid) < m:
                s = mid + 1
            else:
                e = mid - 1
        return ans

