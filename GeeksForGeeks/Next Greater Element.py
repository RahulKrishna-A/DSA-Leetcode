# User function Template for python3


class Solution:
    def nextLargerElement(self, arr, n):
        # code here
        ans = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            # if i==0:
            #         print(stack)
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) != 0:
                ans[i] = stack[-1]
                stack.append(arr[i])
            else:
                ans[i] = -1
                stack.append(arr[i])
        return ans