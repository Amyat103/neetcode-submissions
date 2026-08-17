# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        constaints - empty? min 1, always bin tree, 2 nodes? ok

        1) each level, check if acc = max(acc, curr)
        max left, max right or max left + right
        - each level recalc max, global
        - each level return left or right
        """

        longest = 0

        def dfs(root):
            nonlocal longest
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            longest = max(longest, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return longest