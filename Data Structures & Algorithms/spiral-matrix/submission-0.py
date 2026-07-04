class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        watched solution before trying

        so algo is 4 pointers
        this will be O(n * m)
        where 4 pointers will be left,right,top,down and we traverse by
        top,left, toprihgt, topright, bottom right, bottom right, bottom left, bototm left, top right, but each traverse we update
        after topleft -> top right, top -= 1, so dynbamically right afte rthis if we start topright to bototm right
        we elimitate the duplicate top with top -=1 and shink dynamically
        also append answer
        shrink right after each loop
        """
        # 0, 2, 0, 2
        top,down = 0, len(matrix)
        left,right = 0, len(matrix[0])
        ans = []

        while top < down and left < right:
            #append first row left-> right
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            #append last col, up to down
            for i in range(top, down):
                ans.append(matrix[i][right-1])
            right -= 1
            if (not top < down or not left < right):
                break
            #append matrix bottom row right to left
            for i in range(right-1, left - 1, -1):
                ans.append(matrix[down-1][i])
            down -= 1
            #append matrix left col down to top
            for i in range(down-1, top - 1, - 1):
                ans.append(matrix[i][left])
            left += 1
        
        return ans