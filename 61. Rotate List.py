# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = self.findlength(head)
        if count <= 1:
            return head
        rot = k % count
        s = head
        f = head
        for i in range(rot):
            f = f.next
        while f.next != None:
            s = s.next
            f = f.next

        f.next = head
        head = s.next
        s.next = None
        return head

    def findlength(self, head):
        temp = head
        count = 0
        while temp != None:
            temp = temp.next
            count += 1
        return count