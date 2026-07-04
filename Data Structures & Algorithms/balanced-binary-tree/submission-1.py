# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        use dfs(root)
        if not, reutnr 0
        else return 1 + max(left right)
        if left - right >= 2, return false
        lese true
        """

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if left is False or right is False:
                return False

            if abs(left - right) >= 2:
                return False
            
            return 1 + max(left, right)

        if dfs(root) is False:
            return False
        return True