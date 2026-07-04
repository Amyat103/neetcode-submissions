# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        given root of tree, reutnr deptpth, longest path is depth ok
        aks quesitons, constairnt? empty? i dont think the number matter the node num, only counting depth
        ok im thinking dfs tree traversal, bfs work too but easier for me dfs
        for this will be O(n) O(1) space
        traverrse all nodes, 
        algo will go
        each node, keep going to base case, empty, reutnr 0, and each lvl retunr 1 +
        at the end reutrn largest max()
        """
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return 1 + max(left, right)
        
        return dfs(root)