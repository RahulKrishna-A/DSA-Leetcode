# User function Template for python3


class Solution:

    # Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self, a, n):
        # code here
        stacks = []
        ans = [1] * n
        for i in range(n):
            cur_ans = 1

            while stacks and stacks[-1][0] <= a[i]:
                cur_ans += stacks[-1][1]
                stacks.pop()
            stacks.append([a[i], cur_ans])
            ans[i] = (cur_ans)
        return ans