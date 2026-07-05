class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        mxn - might not square
        ans = [] < append to ans
        can matrix be empty? no min 1 ok
        think 2 mthods
        1) i do a dfs until i reach the end
        seen set(), direction = [4dir]
        dfs(from 0,0) while dfs(next dir) valid, keep going OR dfs(next dict) is seen, then turn until cant turn anymore
        2) 4 pointers method where top,down,left,right 4 loops
        for left,right, top down,.... append to ans
        each while loop, -=1 for internal traversal
        both these are O(n*m) time, need to go throguh everything
        sapce is also n*m need to store everything
        """
        ans = []

        top,bottom = 0, len(matrix)
        left,right = 0,len(matrix[0])

        while top < bottom and left < right:
            #4 loop base on direcitons
            for i in range(left, right):
                ans.append(matrix[top][i])
            
            top += 1

            for i in range(top, bottom):
                ans.append(matrix[i][right-1])
            
            right -= 1
            #check if same 
            if top < bottom:
                for i in range(right-1,left-1,-1):
                    ans.append(matrix[bottom-1][i])
            
            bottom -= 1
            
            if left < right:
                for i in range(bottom-1, top-1,-1):
                    ans.append(matrix[i][left])
            
            left += 1

        return ans