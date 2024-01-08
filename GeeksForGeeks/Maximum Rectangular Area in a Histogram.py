# User function Template for python3


class Solution:

    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, arr):
        # code here
        stack = []
        max_area = 0

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                height = arr[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        while stack:
            height = arr[stack.pop()]
            width = len(arr) if not stack else len(arr) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area

