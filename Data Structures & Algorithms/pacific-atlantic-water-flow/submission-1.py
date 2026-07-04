class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        find all cells where water can get into pacific and atlantic
        return 2d list of each cell as [r, c] any order

        keeping an ans array, and pacific set, and atlantic set
        run bfs,dfs twice, one from pacific, one from atlantic,
        at the end if exist in atlantic and pacific put into ans

        dfs
        pacific, first row or first col, so for heights[0][...] heights [...][0]
        dfs, all 4 direction, if not in seen + higher, go and add into pacific

        atlantic, same but heights [-1][....], heights[...][-1]
        dfs, all 4, if not seen + higher, go and add into atlantic set

        ocean.add()
        """
        ans = []
        pacific = set()
        atlantic = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(ocean, row, col):
            ocean.add((row, col))
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r,c) not in ocean and r < len(heights) and c < len(heights[0]) and r >= 0 and c >= 0 and heights[r][c] >= heights[row][col]:
                    dfs(ocean, r, c)
        
        for row in range(len(heights)):
            dfs(pacific, row, 0)
            dfs(atlantic, row, len(heights[0]) -1)
    
        for col in range(len(heights[0])):
            dfs(pacific, 0, col)
            dfs(atlantic, len(heights) - 1, col)
        
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in atlantic and (row,col) in pacific:
                    ans.append([row, col])

        return ans
