# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        given binary tree, invert, ok invert means, from teh root swapping left right, each subtree also swap?
        looking at pic, maybe interviewere ans, yes ok i see
        ask quesiton, anyu constriant? empty tree? do i have to wrory about nums? or just swapping
        thinking about apprach im thinking i do a dfs, i dont think bfs matter, just need to visit all nods, and swap childs
        so i choose dfs easier for me. and thiknig about it empty node, unbalance i cna swap node <> empty seem to wrok, ill do taht
        this apprach wil be O(n) need to visit all nodes, and swap ok
        anything im mising? hint? 
        ok should i tupe it up?
        """
        def dfs(root): #not sure if god rpactice or just use invertTree and self. but this easier
            if not root: #abse case
                return None
            left = root.left
            right = root.right
            root.left = right
            root.right = left

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root