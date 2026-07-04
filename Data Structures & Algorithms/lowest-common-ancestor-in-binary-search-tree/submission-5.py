# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        input: node, head of a BST, and p and q 2 nodes
        return: the LCA of two node

        ask? empty? no at least 2 node in tree || what about negative? yes, -100
        q and p unique

        BST -- node 2 child, left < node, right > node

        dfs algo, lowest node, NOT the lowest value, base on level? not val

        dfs algo 3 cases
        1) p and q are right AND left -> return node
            ALSO include if q is node, or p is node, THEN also return
        2) p and q are BOTH < node -> go left
        3) p and q are BOTH > node -> go right
        """

        def dfs(root):
            if p.val < root.val and q.val < root.val:
                return dfs(root.left)
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right)
            else:
                return root
        
        return dfs(root)