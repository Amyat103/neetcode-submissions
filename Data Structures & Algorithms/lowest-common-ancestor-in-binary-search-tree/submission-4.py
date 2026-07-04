# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        BST -- binary (2 child), st, left < node < right
        since bst, algo can be O(log n?) 1 path

        algo 
        node, if both < go left, if both > go right
        else return, (catch if either one is the LCA) also catch if they are split
        """

        def dfs(root):
            if root.val < q.val and root.val < p.val:
                return dfs(root.right)
            elif root.val > q.val and root.val > p.val:
                return dfs(root.left)
            else:
                return root
        
        return dfs(root)