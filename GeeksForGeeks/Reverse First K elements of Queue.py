# User function Template for python3
'''
Function Arguments :
		@param  : q ( given queue to be used), k(Integer )
		@return : list, just reverse the first k elements of queue and return new queue
'''
from collections import deque


# Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        # code
        q = deque(q)
        stack = []
        size = len(q)
        for i in range(k):
            ele = q.popleft()
            stack.append(ele)

        while len(stack) != 0:
            ele = stack.pop()
            q.append(ele)
        for i in range(size - k):
            ele = q.popleft()
            q.append(ele)
        return q
