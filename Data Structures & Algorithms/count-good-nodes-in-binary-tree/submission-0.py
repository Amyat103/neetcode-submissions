# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        can tree be empty? no ok negatives?
        min 1, yes neg? ok

        ans = 0, increment as i go if matches constraitns
        dfs(node, highest): if curr >= highest, ans +=1, 
        # check condition, inc
        # update max() if needed
        need gloabl ans, +=1
        """
        ans = 0

        def dfs(node, highest):
            nonlocal ans
            if not node:
                return
            if node.val >= highest:
                ans += 1
                highest = max(highest, node.val)
            dfs(node.left, highest)
            dfs(node.right, highest)
        
        dfs(root, float("-inf"))
        return ans