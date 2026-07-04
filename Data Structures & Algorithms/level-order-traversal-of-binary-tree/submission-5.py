# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        input: root of binary tree, return level order nested list

        algo: bfs algo, with ans = []
        att root in, for _ in len(queue), make a new list for that levle []
        popleft and append to taht level, for each node, apend child to queue again
        return ans
        """
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(level)

        return ans