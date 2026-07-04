# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
        after = curr.next
        curr.next = None
        prev = None
        curr = after
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        left, right = head, prev
        dummy = ListNode(0)
        while left and right:
            dummy.next = left
            dummy = dummy.next
            left = left.next
            dummy.next = right
            dummy = dummy.next
            right = right.next
        dummy.next = left
