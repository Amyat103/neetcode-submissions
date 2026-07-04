class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        n: int, edges [[int,int]]
        return # connected graph
        constraint ask: empty? no min 1, no repeated edges, all item in edge 2 item
        1) first thing think is teh way graph is in list, make a dict
        key: start, list[end]
        then from there, i can dfs,
        for i in range n, if not in seen dfs, ans += 1
        this way its still O(n) cleanly processed
        """
        ans = 0
        graph = {}
        seen = set()

        #make graph, key start, list of end vals
        for e1,e2 in edges:
            if e1 not in graph:
                graph[e1] = []
            if e2 not in graph:
                graph[e2] = []
            graph[e1].append(e2)
            graph[e2].append(e1)

        print(graph)
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
        
        for i in range(n):
            if i not in seen:
                if i in graph:
                    dfs(i)
                ans += 1
        
        return ans