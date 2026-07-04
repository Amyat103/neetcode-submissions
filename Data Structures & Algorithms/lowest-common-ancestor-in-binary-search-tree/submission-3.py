# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        given bst, all val unique, and also p,q nodes, 
        return lowest common ancestor, 
        ok so exmaple 7,9 is 8, 1,4, is 3, 2,7 is 5 ok 
        ask quesitons -- any edge cases, empty tree? ok ,
        all nodes are int? no have to consider non int? ok
        negative? actually dont matter for bst
        and bst are valid ok
        # 1, seeing the term bst make me think if i can solve in log n
        since its sorted and left right, let me think, 
        O(n) is solvable but log n
        if i traverse say 
        ok 1 more questoin is q larger than p, could mke it simpler
        doenst say in quesiton, assume interview dont say anything ok wont assyume that then
        currently thining algo like:
        i can traverse if curr > q and curr > p, then left side, right too big
        if curr < q and curr < p, then right, left too small dont consider
        and if curr>p and curr < q or curr < p and curr > q, then they are right left, this si smallest
        currnetly thikng about this
        since dont have  to consider empty, if qp dont exist and p!= q in ans, think this owkr
        ask -- is tehre sth not considering? or not seeing..... (dik if i shoudla sk but)
        ok illl code up
        wait the time space is 
        O(log n) time space O(n) worst, cuz ill dfs, and stack limit
        """
        def dfs(root):
            if root.val < q.val and root.val < p.val:
                return dfs(root.right)
            elif root.val > q.val and root.val > p.val:
                return dfs(root.left)
            else:
                return root
        return dfs(root)