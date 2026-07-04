class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        given a 2d array grid
        graph traversal, where i can dfs somehow
        and return -1 or time
        constraint - empty arr? whats min len? 1 ok, itll only be 012 ok
        1) go throuhg all of them, if its 2 dfs into it and acc and time var starting 0 += 1...
        dont work cuz cant fully dfs into 1, wrong time, if multiple rotten
        2) go through put all rotten into a queue(), bfs traversal
        go toughe ach rotten, append the next door fresh, time += 1
        non fresh left return time if all gone, else return -1
        maybe i keep a fresh set(), of row and col, so i can if not fresh return time else return -1
        O(n * m) -- time and space
        """
        time = 0
        #dont need seen cuz i can change fruit in place
        rotten = set()
        fresh = set()
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        #pre process, put all in accordily
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue:
            #need to loop through the len(for this level)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                #go through all 4 chck constraitsn and traverse
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row >= 0 and col >= 0 and row < ROWS and col < COLS and (row,col) in fresh:
                        #rot it
                        fresh.remove((row,col))
                        queue.append((row,col))
            if queue:
                time += 1

        return time if not fresh else -1