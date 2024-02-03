class Solution:
    # Function to return list containing elements of right view of binary tree.
    def rightView(self, root):
        if root == None:
            return root
        qu = deque()
        qu.append(root)
        answer_list = []
        while qu:
            curr_len = len(qu)
            for i in range(len(qu)):
                curr_ele = qu.popleft()
                if i == curr_len - 1:
                    answer_list.append(curr_ele.data)
                if curr_ele.left:
                    qu.append(curr_ele.left)
                if curr_ele.right:
                    qu.append(curr_ele.right)
        return answer_list

