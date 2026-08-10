class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Q: all digits? can it be string and invaldi?
        len alwyas 9 ok
        1) go thorugh all, check if n exist in row/col/box, return false 
        end return true
        3 dictionaries for O(1) cehcks
        """
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set) #(r,c) key

        for r in range(len(board)):
            for c in range(len(board[0])):
                curr = board[r][c]
                if curr != "." and (curr in row[r] or curr in col[c] or curr in box[(r//3, c//3)]):
                    return False
                row[r].add(curr)
                col[c].add(curr)
                box[(r//3), (c//3)].add(curr)
        
        return True