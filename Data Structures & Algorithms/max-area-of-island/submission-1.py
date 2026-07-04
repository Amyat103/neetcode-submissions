class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        outside the grid all water, it can only be 0 1, numbers, not string
        can it be emtpy? no at least 1 ok
        need sth to track biggest var: ans
        go in and see all island need a dfs(r,c), traverse until see all land, ans = max(ans,ladn) ...
        to track it might have to use dfs(r, c, curr),
        need a outer loop for dfs, go throuhg all blocks, 
        if grid rc == 1, dfs(into it), 
        need a seen save time and not double count
        """
        ans = 0
        seen = set() #set of pairs (r,c)

        def dfs(r,c):
            #not in bound return 0
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or (r,c) in seen:
                return 0
            #in bound, reutnr 1 + all path
            seen.add((r,c))
            return (1 + 
                    dfs(r+1,c) +
                    dfs(r-1,c) +
                    dfs(r,c+1) +
                    dfs(r,c-1))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in seen and grid[r][c] == 1:
                    ans = max(ans, dfs(r,c))
        
        return ans