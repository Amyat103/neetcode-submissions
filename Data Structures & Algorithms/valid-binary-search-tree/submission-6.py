# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        input: root of tree,
        return treu/false if valid BST
        constriant:1)left subtree of every node only node with keys less than node
        2) right subtree of every node contians only node more than node key
        3) both left and right ar ealso BST
        ok any cosntiatns? non int? negative(neg dont matter dont mention), all nums, can be neg ok
        #1 im thinking of a dfs apprach, feel like as long as i traverse d or b dont matter so ill d
        dfs( im thinking a ) for each root, if root.left > root or root.rightg < root, return false, else contineu
        if emprt return true, and doa  return left AND right, to cehck true/false
        am im isisng anything this would be a O(n) algo with O(n) psace for call stacl
        oh halway realize what if node val are same ill ask that, but queiston dont state so ill act as if interviwere say cant say ok
        """
        def dfs(root, left, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            
        return dfs(root, float("-inf"), float("inf"))
