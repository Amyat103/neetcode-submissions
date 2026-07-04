# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            2
        1       3
        05      1,6
        input: root of tree
        ouput: true/false if bin tree
        Binary Tree: each node 2 edges, left < node < right
        ask = same val in treee? no | empty? yes | neg dont amtter ok
        algo is a dfs() where check each side
        if .left||.right check if < >, and dfs into
        return True, Fasle up to top
        BUT, need casese where a left sub tree is higher than root
        since dfs dont remmber need to pass down a max min val 
        where subtree need to fall under
        algo, dfs(min, max, node)
        check left < node < right ALSO
        node < max, node > min
        init at float("-inf") and float("inf")
        """
        def dfs(low, high, node):
            # check in bound
            if not node:
                return True
            elif not (low < node.val < high):
                return False
            return dfs(low,node.val,node.left) and dfs(node.val,high,node.right)
        
        return dfs(float("-inf"), float("inf"), root)







