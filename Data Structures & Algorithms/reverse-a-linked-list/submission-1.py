# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        con - LL can be empty
        curr, next, prev
        curr, 0 next 1, prev at before curr = None
        curr.next = prev
        prev = curr
        curr = next
        next = next.next

        return curr
        """
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev