class Solution:
    def findMax(self,root):
        #code here
        maxs =  -float("inf")
        qu = deque()
        qu.append(root)
        while qu:
            for i in range(len(qu)):
                cur = qu.popleft()
                if cur.data>maxs:
                    maxs=cur.data
                if cur.left:
                    qu.append(cur.left)
                if cur.right:
                    qu.append(cur.right)
        return maxs
    def findMin(self,root):
        mins =  float("inf")
        qu = deque()
        qu.append(root)
        while qu:
            for i in range(len(qu)):
                cur = qu.popleft()
                if cur.data<mins:
                    mins=cur.data
                if cur.left:
                    qu.append(cur.left)
                if cur.right:
                    qu.append(cur.right)
        return mins
