# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        input root, reutrn true false, iunput 2 roots if same or diff
        not same as in node == node but same value ok
        ask -- any constraitns, empty, waht about non int, ar ethey all int, equal, str == str? ...
        neg val not really constaint cuz if int
        ok so can be empty, ok can be neg, no string ok
        #1 approach im tinking breth? just top of head seem easier, append them into deque, and pop
        dfs recursion ned to handle 2 tree seem harder
        some cases are need to cehck before we start, check base
        start bfs, for each level pop the item at teh level, and for_in (,2 ) skip by 2
        """
        #base check
        if p and not q or q and not p:
            return False
        
        def dfs(p, q):
            if not p and not q:
                return True
            elif p and not q or q and  not p:
                return False
            elif p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p,q)

        
        

