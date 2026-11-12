class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        init 3 dict, kepe adding and checking
        break loop and false if seen, else return treu at last
        """
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                curr = board[r][c]
                if curr in row[r] or curr in col[c] or curr in square[(r//3, c//3)]:
                    return False
                row[r].append(curr)
                col[c].append(curr)
                square[(r//3, c//3)].append(curr)
        
        return True