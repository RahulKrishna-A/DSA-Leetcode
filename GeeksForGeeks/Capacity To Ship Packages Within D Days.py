class Solution:
    def leastWeightCapacity(self, arr, N, D):
        # code here
        def canCarry(max_weight):
            weight = 0
            days = 1
            for i in range(N):
                if weight + arr[i] <= max_weight:
                    weight += arr[i]
                else:
                    weight = arr[i]
                    days += 1
            return days

        s = max(arr)
        e = sum(arr)
        while s <= e:
            mid = s + (e - s) // 2
            if canCarry(mid) <= D:
                e = mid - 1
            else:
                s = mid + 1
            # print(s,e,mid)
        return s