# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        given a root, return diameter -- longest path between 2 nodes
        binary tree- left, right , 2 child at most, 

        dfs() -- go .left .right,
        return dfs(left) + dfs(right) + 1), max(dfs(lefT), dfs(right))

        ans = 0
        dfs(left) + dfs(right), > ans, ans = 
        return 1,
        each tiem return max(dfs(left), dfs(rigiht)), change ans if >
        time: O(n)
        space:(1)
        """
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            if left + right > ans:
                ans = left + right
            return 1 + max(left, right)
        
        dfs(root)
        return ans