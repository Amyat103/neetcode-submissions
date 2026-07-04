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
        NOTE: just watched a vid, and redoing, will try to explain all so that i now pattern and logic and not just ememorize
        given: node ina  undirected graph
        return deep copy- copy each node adn neighbor
        undirected, connected both way, so if input is self.neighbors with list of nodes [nodes] then if 4<> 1 4:[1] 1:[4]
        ok, ask quesitons impotant -- any constaints, can it be empty?, yes? ok so can be empty, cant think of other questions
        ok i see so i need to traverse a given node, which has .val and .neighbors, traverse the graph and make deep copy,
        #1) im think a dfs() algo, start with a node, make a copy, look at node list, copy its nodes ... ercursively add add
        time will be O(n) visit each node once, visit every, space is O(n) each node iwll be in dict{}
        oh need a dict to, to store that weve created node, or else we keep making new one cant track, cant use seen set() cuz need to map it
        anything im missng? or gettign wrong?
        """
        oldNew = {}

        #dfs algo
        def dfs(node):
            #cases, if exist return that new node of this old node
            #if dont exist, create and return new node
            #if dont exist that mean first time seeing, so also need to traverse its neighbors
            if node in oldNew:
                return oldNew[node]
            
            #now if dont exist
            copy = Node(node.val) #create new node with same val
            oldNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        if node:
            return dfs(node)
        else:
            return None