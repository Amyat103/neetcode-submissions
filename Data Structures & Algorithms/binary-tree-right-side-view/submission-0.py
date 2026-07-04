# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        input: bin tree, 2 nodes, left right, return right view
        list[nums]
        problem: traverse and find whats visible from right side
        dfs() dont work 
        bfs(), go through eac level, take [-1] last one, append that one

        ans = []
        bfs() append to queue
        time: O(n) go throughe very node
        space: O(n) at most, everyones in ans

        forgot to ask -- empty? yes 
        """
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            #get the alst one for each level
            ans.append(level[-1])
        return ans
            