class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        input: m x n matrix
        output the same matrix, change in place, if ele is 0, set row col 0
        questions: can it be empty, m x n? [[1]] min
        for .. in m
            for ... in n
            if matrix m n == 0, row.add col.add
        for .. in m
            for ... in n
            if m in .. or n in ... matrix == 
        row = []
        col = []
        """
        rows, cols = len(matrix), len(matrix[0])

        rowZero = [False] * rows
        colZero = [False] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowZero[row] = True
                    colZero[col] = True
        
        for row in range(rows):
            for col in range(cols):
                if rowZero[row] == True or colZero[col] == True:
                    matrix[row][col] = 0
