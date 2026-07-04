# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        all ints, non empty lls
        add them, already in reverse order

        traverseing 2 pointers, head to tail
        have a carry var, to add
        l1 = [9], l2 = [9], if carry: .next = Node(carry)
        at the end of 2 pointer, need to add a if l1 or l2 incase non matching lenght
        grab digit
        sum // 10, == grab carry
        sum % 10 == grab least sig
        """
        carry = 0
        ans = ListNode(0)
        trav = ans

        while l1 or l2 or carry:
            #trick is if addition
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10
            trav.next = ListNode(total)

            trav = trav.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ans.next