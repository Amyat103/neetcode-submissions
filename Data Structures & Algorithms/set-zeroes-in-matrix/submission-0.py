class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        watched solution

        given mxn if element is 0, set its row and col 0
        brute force is make a copy, of matrix

        then loop original, if rc == 0, call a helper, go modify copy, at the end return copy
        n*m + n+m or sth cuz worst case for each one, loop rowcol

        but a better solution is to use 2 array len(matrix) and len matrix[0]
        and one call row adn 1 call col where false by default, go through original array, if matrix[r][c] == 0
        then row[r] = true, col[c] = true,
        tehn a final loop after this pre process where, if row[r] or col[c], matrix[r][c] == 0
        this makes it O(n*m)
        space is o(n+m)
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        row,col = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row[r] = True
                    col[c] = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if row[r] or col[c]:
                    matrix[r][c] = 0
