class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        can it be empty? a empty list? always return a ordered list and always start 0,0
        1) dfs(r,c), always start 0,0, keep going and appending, until OOB or seen turn
        2) 4 pointers, 4 loops nested inside a while loop 
        cleaner to track, i just -=1,+=1 
        O(n*m) traveseing all once
        space: O(n*m) becuase sotreing all once
        """
        ans = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #go 4 directions and shrink
            for i in range(left, right):
                ans.append(matrix[top][i])

            top += 1
            
            for i in range(top, bottom):
                ans.append(matrix[i][right-1])
            
            right -= 1
            if not (left < right and top < bottom):
                break
            
            for i in range(right-1, left-1, -1):
                ans.append(matrix[bottom-1][i])
            
            bottom -=1
            
            for i in range(bottom-1, top-1, -1):
                ans.append(matrix[i][left])
            
            left += 1

        return ans