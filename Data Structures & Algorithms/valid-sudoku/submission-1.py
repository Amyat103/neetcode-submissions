class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        given board, each row, col, box, can onyl contain 1-9, no dup
        return true/false

        ask--1-9 / . string, can it be anything else do i need to check? no only 1-9 or . ok
        board always 9x9 and its 2d array? ok

        1) first thing come to mind, check all 3 condiiton separately, brute force, run 3 algo?
        for each col, loop through each col, return true if all true
        for each row, same as above, return true if all true,
        for each box, ...
        2) but should be able to solve running once, and checking seen?
        if i have 3 set of seen variabes, for each of the three, row, col, box, and store (r,c) grid

        I will have 1 main double loop, go through r, c
        each one i go throuhg ill add to the seen,
        row seen.add(r)
        actually need to be dictionary because need to mark key for row,col,box, and value is the num for that row
        go through each one,
        everytime we see non ".",
        check if digit alreayd in one of the 3 dict, return False immedietly, or lse  
        do 3 things
        add digbit to 3 dictionary, row_seen,col_seen,box_seen
        return true at end
        Time: O(n * m) go through all boxes
        Space: O(n*m), at most all fill and corect, and need to sotre all
        """
        rowSeen = defaultdict(set)
        colSeen = defaultdict(set)
        boxSeen = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                # check 3 condoiton for false, return
                curr = board[r][c]
                if curr != ".":
                    if curr in rowSeen[r] or curr in colSeen[c] or curr in boxSeen[(r//3, c//3)]:
                        return False
                    
                    rowSeen[r].add(curr)
                    colSeen[c].add(curr)
                    boxSeen[(r//3,c//3)].add(curr)
                
        return True