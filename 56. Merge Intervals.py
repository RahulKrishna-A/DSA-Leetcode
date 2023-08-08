class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        ans = [intervals[0]]
        for points in intervals:
            if points[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], points[1])
            else:
                ans.append(points)

        print(ans)
