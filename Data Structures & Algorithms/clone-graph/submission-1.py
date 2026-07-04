"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Deep copy, dfs
        alrogiuthem is
        using dfs traverse all teh nodes, during traversal
        1) if node not been created, make it
        else, return copied of that node in mapped {}
        2) loop through .nrighbors of node and for each
        copy.neighbors.append(dfs(neighbor)), adding nodes to copied, but not originak
        adding new ones, since only new nodes are retuend not old
        """
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node) if node else None


