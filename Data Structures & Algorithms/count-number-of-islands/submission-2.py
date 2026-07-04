class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        input type: 2d array, as graph, traverse with indexing [row][col]

        1 is land 0 is water, count num island
        so dfs algo where for each island start somewher, traverse, add to seen, and reutnr
        outer loop track counts, so += 1 everytime we dfs, cuz that mean island

        """
        ans = 0
        seen = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            seen.add((row, col))
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # go into dfs if land and not traversed yet
                if (row, col) not in seen and grid[row][col] == "1":
                    dfs(row, col)
                    ans += 1
        
        return ans