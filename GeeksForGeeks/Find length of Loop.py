#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    #Your code here
    s= head
    f=head
    flag=1
    while f!=None and f.next!=None:
        s=s.next
        f=f.next.next
        if s==f:
            flag=0
            break
    if flag:
        return 0
    dummy = s.next
    count=1
    while dummy!=s:
        dummy=dummy.next
        count+=1
    return count