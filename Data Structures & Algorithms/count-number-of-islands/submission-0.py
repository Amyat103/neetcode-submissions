class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        input in 2d grid, 1 is ladn 0 is water, 2d graid is list[list[]] inside strs ok
        return # island, island are same if tehy connected updownleftright
        edge are water ok
        ask questions, so can only be str of 0 and 1? ok no edge cases for that,eprt ggrid? at elast 1len() ok
        #1 im thinking traversing 2 depth
        so outer loop, go through each item in grid, for i .. for j, 
        adn inside if we touch land == 1, tehn we will traverse, go inside, left right up down, traverse
        using dfs()
        so algo will be traverse all items in grid, but since its list[list] its O(n^2) ? since 
        even through we only touch it once, still list[list]
        and not more thant n^2 cuz we keep a seen so no extra traverse
        space is O(n^2) track all in seen
        anything missing? aks any 
        """
        # try to come up with eveyr var
        seen = set()
        ans = 0

        # added later but ill say oh ill need directions to amke it easier
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] != "1" or (i,j) in seen:
                return
            seen.add((i, j))
            for dir_row, dir_col in directions: # go 4 directions
                row, col = dir_row + i, dir_col + j
                dfs(row, col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #if land go in else skip
                if grid[i][j] == "1" and (i, j) not in seen: # need not in seen so only count once and dont go in adn recount
                    dfs(i,j)
                    seen.add((i, j))
                    ans += 1

        #so the algo is go throuhg all i  and j, if not in seen: go in, and inside we add things to seen so 1 are not recounted

        return ans