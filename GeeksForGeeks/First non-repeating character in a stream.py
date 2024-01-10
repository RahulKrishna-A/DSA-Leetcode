# User function Template for python3
from collections import deque


class Solution:
    def FirstNonRepeating(self, A):

    # Code here
    hashma = {}
    ans = ""
    qu = deque()
    for i in A:
        if i not in hashma:
            hashma[i] = 1
            qu.append(i)
        else:
            hashma[i] += 1
        while len(qu) > 0 and hashma[qu[0]] > 1:
            qu.popleft()
        if len(qu) > 0:
            ans += qu[0]
        else:
            ans += "#"
    return ans
