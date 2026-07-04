class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        given a grid, replace all land cell with distance to treasure

        start nested loop, traverse all item in grid, if 0, initalize dfs()
        dfs(), start at treasure, +1 each time it goes out (only go out if land AND not seen)
        replace land with whatever +1
        dfs(r, c, distance)
        Time: O(n * m)
        space: O(n*m) seen variables set()
        ask, empty grid? always treasures? all ints? no empty grid at least 1, always int ok
        """
        # seen = set()
        directions = [(0,1), (0, -1), (1,0), (-1,0)]

        def dfs(r, c, distance):
            grid[r][c] = min(grid[r][c], distance)
            # seen.add((r,c))

            for dr, dc in directions:
                row = dr + r
                col = dc + c

                if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and (grid[row][col] != -1 and grid[row][col] != 0) and (distance + 1) < grid[row][col]:
                    dfs(row, col, 1 + distance)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: #treasure start
                    # seen = set()
                    dfs(r, c, 0)