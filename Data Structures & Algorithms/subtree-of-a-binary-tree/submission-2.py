# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            if checkSub(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        def checkSub(first, second):
            if not first and not second:
                return True
            elif first and second and first.val == second.val:
                return checkSub(first.left, second.left) and checkSub(first.right, second.right)
            else:
                return False
        
        return dfs(root)