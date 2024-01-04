# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''


class Solution():
    def mergeLL(self, node1, node2):
        dummy = Node(0)
        temp = dummy
        while node1 and node2:
            if node1.data < node2.data:
                temp.bottom = node1
                node1 = node1.bottom
            else:
                temp.bottom = node2
                node2 = node2.bottom
            temp = temp.bottom
        if node1:
            temp.bottom = node1
        else:
            temp.bottom = node2
        return dummy.bottom

    def flatten(self, root):
        # Your code here
        if root == None or root.next == None:
            return root

        root.next = self.flatten(root.next)

        return self.mergeLL(root, root.next)