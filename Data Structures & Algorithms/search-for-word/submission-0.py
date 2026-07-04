class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        input: board [[char]] 2d char, and string word
        return: true/false if word exist in board, by path
        ask? can it go all 4 dire? yes | empty? no

        ok NOT dp cuz noy building up to rest
        constraint: same cell cant use once

        algo is backtrack explore all possibility and return treu false with dfs
        dfs(), will have r, c, i
        i - index of word were at, and 
        case 1: if i >= Len(wrod)? return True, cuz past last index
        case 2: if r, c out of bound, or word[i] !== board[r][c], or (r,c) already seen: FASLE
        after 2 if, check all 4 direction
        and return with 
        res = dfs(up) or down or left or right
        seen.remove((r,c)) # backtrack need to rmeove those so fresh path
        return res
        loop double for, dfs each letetr
        """
        seen = set()

        def dfs(r, c, i):
            if i >= len(word):
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0])) or word[i] != board[r][c] or (r,c) in seen:
                return False
            seen.add((r,c))
            res = (dfs(r+1, c, i + 1) or
                    dfs(r-1, c, i + 1) or
                    dfs(r, c+1, i + 1) or
                    dfs(r, c-1, i + 1))
            seen.remove((r,c))
            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        
        return False