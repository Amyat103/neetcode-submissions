class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        gonna watch vid instantly but for this brute seem like for each islnd keep going to see if reach edge, brute force
        watching vid...

        watched vid

        input: 2d array heights, heights[r][c] is height of that location
        left and top is pacific bottom and right is atlantic
        watter can go all 4 dir, but only move when height == or less than curr
        return location where it can reach both top/left or bottom/right

        ask constraitnss? any neg? emprt arr??
        no emprt arr, at least len 1, ok and no neg at min is 0 ok

        #1 brute is to go through each cell, for that cell run a dfs where return true if it can reach both. add to ans
        but that would be O(n*m) * n*m so n*m) ^2,

        #2 use borders adn start building in, start from say topbot rows, left right cols, adn mvoe in. add everything
        that can reach border to set, move in with opposite checks

        algo goes like:
        from top row or bot rows, if within bounds, if not more than prev, add to visited
        from left col or right col, if in bound, if not more than prev, add to visited

        at teh edn run a check for all cell, if cell in both seens, add to ans

        solution os O(n*m), it go through n*m 3 times but still n*m, no power
        space is n*m too 
        """
        #starting ill need ans[], rows,cols, and 2 seen/visited
        ans = []
        rows,cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, seen, prev):
            #validate, if in range, and if prev is < (checking backward) and not in seen
            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in seen:
                return
            if prev > heights[row][col]:
                return
            seen.add((row, col))
            # go 4 directions
            dfs(row+1, col, seen, heights[row][col])
            dfs(row, col+1, seen, heights[row][col])
            dfs(row-1, col, seen, heights[row][col])
            dfs(row, col-1, seen, heights[row][col])


        #traverse left and right
        #go into first item of each row
        #go in last item of each row
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0]) #go into 0,0|1,0|2,0 left row
            dfs(row, cols-1, atlantic, heights[row][cols-1]) #go into 0,-1|1,-1|
        
        #traverse top and bot
        #go into all item in first row
        #go into all item in last row
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col]) #go into 0,0|0,1|0,2|0,3|...
            dfs(rows-1, col, atlantic, heights[rows-1][col]) #need 0,-1|0,-2|0,-3

        # find in both adn add
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    ans.append([r,c])

        return ans




