# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def mergeTwo(first, second):
            dummy = ListNode(0)
            ans = dummy
            one, two = first, second
            while one and two:
                if one.val < two.val:
                    dummy.next = one
                    one = one.next
                else:
                    dummy.next = two
                    two = two.next
                dummy = dummy.next
            if one:
                dummy.next = one
            if two:
                dummy.next = two
            return ans.next
        
        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i+1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                mergedList.append(mergeTwo(l1, l2))
            lists = mergedList
        return lists[0]

