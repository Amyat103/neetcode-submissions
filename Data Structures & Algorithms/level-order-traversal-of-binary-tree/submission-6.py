# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        input: root, of binary tree
        output: level order traversal [[]]

        ask = empty? yes can be | ok thats all constraitns 

        algo traverse every node in the tree
        BFS traversal works well here, every elvel init a []
        append after level done, return
        Time: O(n) traverse every node
        Space: O(n) append the val of every node into a new list
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
            ans.append(level)

        return ans




