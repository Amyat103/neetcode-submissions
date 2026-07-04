# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        need to traverse level, so just dfs but order of recursion matters
        if not root, return
        if root, ans.append(root.val)
        if root.left dfs(left)
        if root.right dfs(right)

        so that every new code, left mid right order, append
        """
        if not root:
            return []
        ans = []

        queue = deque([root])

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr.append(node.val)
            ans.append(curr)

        return ans 

                