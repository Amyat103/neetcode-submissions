# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        fast = dummy.next
        slow = dummy

        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False