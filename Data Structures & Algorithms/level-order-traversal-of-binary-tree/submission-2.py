# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        input: binary tree root,
        return level order traverse, of val, in a list of list list[list[int]]
        ok-just to make sur lvl means in this exmaple root first, left, right,ok
        ok ask edge case -- can it be metpy (altorugh dfs should handle this)
        hmm dont care about value, really can be str or ints since care about traverse
        ok no real questions i think

        #1 appraoch i think is a dfs(algo), itll go dfs(root), if not root, return
        else add root.val into ans, then go root.elft, go root,right
        dfs(root.left)dfs(root.right) and this work cuz we traverse and for these quesiton i think
        if left first we just do left,root,right, so root.left.right works
        ask if anything im missing ask if miss anything
        ok i see ill code it up
        oh forgot time, the time is O(n) since we go thorugh all of them to build up, space is O(n)ans array n and acall stack is n

        after startng realized that dfs bad, bfs better, since we want to append it by level, dang
        but ill say oh sorry, i relieazed that bfs better
        algo wil be bit differ,t have an ans array [], traverse using bfs
        so ecah level have a curr [] and add that level, then append ans.apend*curr)
        the  next level
        """
        ans = []

        if not root:
            return []
        queue = deque([root])

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(curr)

        return ans




