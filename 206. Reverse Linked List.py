# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        pres =head
        Next = pres.next
        while pres!=None:
            pres.next = prev
            prev = pres
            pres = Next
            if Next!=None:
                Next = Next.next
        return prev