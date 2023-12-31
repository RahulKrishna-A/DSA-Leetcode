class Solution:
    def thirdLargest(self, a, n):
        # code here
        first = a[0]
        second = -float("inf")
        third = -float("inf")
        for i in range(1, n):
            if arr[i] > first:
                third = second
                second = first
                first = arr[i]
            elif arr[i] > second:
                third = second
                second = arr[i]
            elif arr[i] > third:
                third = arr[i]
            else:
                continue
        return third

