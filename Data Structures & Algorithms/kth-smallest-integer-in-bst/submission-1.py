# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        input: root of BST, int k
        output: kth smallest value (1indexed tree)

        BST- 2 child max, left < right >
        1 indexed tree? 
        k is <= # nodes

        algo
        1) first algo i think of is ordered traversal, so we keep the sorted nature
        keep a sroted aray []
        tehn at he end return arr[k]
        dfs traverse dfs(left), append, dfs(right), so its ordered
        """
        sortArr = []

        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            sortArr.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)
        return sortArr[k - 1]