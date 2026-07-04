class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        input: m, n : int, 2 ints
        output: ways to traverse m x n grid starting 0,0 end m-1,n-1
        given 2 ints, not grid, find how mant ways form 0,0 to m-1,n-1

        ask-can it be 0x0? no at least 1x1 || 0,0 m-1,n-1

        constaint: unique path, only move down or right

        dfs algo, to go throuhg all paths
        dfs(r,c): if (m-1,n-1) return 1
        elif, r > m-1, c > n-1, if they out, return 0, dont add to path
        else: return dfs(r+1, c) + dfs(r, c+1)
        need a seen, can mark all grid as -1, only traverse if -1, else ans is there return
        third case, if r,c != -1, return r,c
        Time: O(n*m)
        space: O(n*m)
        """
        grid = [[-1] * n for _ in range(m)] #make m x n grid with -1

        def dfs(r,c):
            if r == (m-1) and c == (n-1): #reach treasure
                return 1
            elif r >= m or c >= n: #OOB, dont contribute path
                return 0
            elif grid[r][c] != -1:
                return grid[r][c]
            grid[r][c] = dfs(r + 1, c) + dfs(r, c+1) #else return r + d
            return grid[r][c]
        
        return dfs(0,0)

