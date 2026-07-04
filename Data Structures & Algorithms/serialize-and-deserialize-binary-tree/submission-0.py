# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(node):
            if not node:
                ans.append("N")
                return None
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        order = data.split(",")
        # OR nonlocal i
        self.i = 0

        def dfs():
            if order[self.i] == "N":
                self.i += 1
                return None
            new_node = TreeNode(str(order[self.i]))
            self.i += 1
            new_node.left = dfs()
            new_node.right = dfs()
            return new_node
        
        return dfs()
