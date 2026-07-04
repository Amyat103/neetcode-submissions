# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        left = list1
        right = list2
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                curr = curr.next
                left = left.next
            else:
                curr.next = right
                curr = curr.next
                right = right.next
        
        if left:
            curr.next = left
        else:
            curr.next = right
        
        return dummy.next
            