class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        input: 2d grid, "1" = land, "0" = water
        return # of islands
        island = connecting lands by horizontal or vertical, up down left right!
        constraints | Empty graph? no at least 1 | grid can be only "1" or "0"? yes

        graph where traverse land
        Algo: go throuhg each item in grid, double for loop, if 0, skip, if 1, dfs() into that location
        seen - track so dont double count
        ans, += 1 everytime we dfs
        Time comp: O(n * m) traversing shouldnt increase beuase it only go in if 1 and dont redo
        Space is O(1), seen and ans
        """
        ans = 0
        seen = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            #traverse if within bounds and add to seen
            seen.add((r, c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and (row, col) not in seen and grid[row][col] == "1":
                    dfs(row, col)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in seen: # if land & not apart of another island
                    dfs(r, c)
                    ans += 1
        
        return ans