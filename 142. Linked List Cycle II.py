# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        count = -1
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                temp = slow.next
                count = 1
                while temp != slow:
                    count += 1
                    temp = temp.next
                break
        if count == -1:
            return None

        s = head
        f = head
        while count > 0:
            f = f.next
            count -= 1
        while s != f:
            s = s.next
            f = f.next
        return f

        # return count
