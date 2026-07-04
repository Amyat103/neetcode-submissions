class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        count island, connected up down left right, not diag

        loop through all rows and cols, if we hit land 
        1) chek if not seen
        2) dfs into the land and += 1 count, when dfs add seen to all land in dfs

        return count
        """
        ans = 0
        seen = set()
        directions = [(0, 1),(1, 0),(0, -1),(-1, 0)]

        def dfs(r, c):
            seen.add((r,c))
            # go 4 dir
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row >= 0 and col >=0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == "1" and ((row,col) not in seen):
                    dfs(row, col)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # if land and not seen + 1
                if grid[r][c] == "1" and (r,c) not in seen:
                    ans += 1
                    dfs(r, c)
        
        return ans
        
