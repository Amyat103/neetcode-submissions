class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        given a board m x n, only contain X and O
        capture region that are sourrounded 
        ask -- only that X capture O? empty? only contain XO? ok, at least len(1)

        this feel like a problem where i need to traverse all region
        if a region is O, il dfs into it
        keep a curr set() maybe of all (r,c), and 
        if it pass, all checks, then sourrounded, chenge all to X,
        check are
        1) never the case that a node is a border
        2) return true if all non border and have a loop that change
        all curr, from O to X
        reset curr each time we dive in a dfs() from outer loop
        keep a seen 
        feel like this is a O(n*m), the loop curr is not significant
        space O(n*m)
        """
        seen = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c, curr):
            safe = True
            if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                safe = False
            seen.add((r,c))
            curr.add((r,c))
            
            for dr, dc in directions:
                row = dr + r
                col = dc + c
                if row > 0 and col > 0 and row <= ROWS -1 and col <= COLS - 1 and board[row][col] == "O" and (row,col) not in seen:
                    if not dfs(row, col, curr):
                        safe = False
            return safe

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and board[r][c] == "O":
                    curr = set()
                    if dfs(r,c, curr):
                        for row,col in curr:
                            board[row][col] = "X"
