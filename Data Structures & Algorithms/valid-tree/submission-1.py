class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        watched vid instaly 

        graph valid tree input n, int
        edges. array of lists, consiting of undirected nodes, so neighbors

        so what i need to do is graph it, like other graph problem, its not given
        so need to make a graph, a defaultdict(list), and tehn traverse it,

        didnt give def of tree, but a tree is connected nodes, with no loop, and all connected

        so nede to loop, if loop aka seen ebfore turen false, else conitnue tiull none, none is true

        and make sure connected by doing a seenlen = n
        algorithm wil lgo,
        1_ buuild graph,
        2_ loop through graph, add curr to seen, visit all neighbors, if curr in seen, return false, else add to seen
        3_ return true/false
        """
        #build graph
        graph = defaultdict(list)
        seen = set()

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        #dfs algo go into each node
        def dfs(node, prev): # needs prev to not go back to rpev, which will return false even if valid
            if node in seen:
                return False #visit before
            
            seen.add(node)

            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                elif not dfs(neighbor, node):
                    return False #if any$0 return false, its not valid whole thign false
                
            return True #all true

        return dfs(0, -1) and (len(seen)) == n

