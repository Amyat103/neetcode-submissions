class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        input m x n matrix, of ints, return a list within matirx aprial order
        so input is 2d m x n, return 1 array of it in order

        ask? can it be empty, ? so smallest [[1]] 1x1 matrix?
        
        example, [[1,2,3],[4,5,6]]
        output [1,2,3,6,5,4]

        4 edges,
        left, right, top, bottom
        for i in left, right.. append (matrix[top][i])
        for i in top, bottom .. append (matrix[i][right])
        for i in right, left Backward .. apppend (matrix[bottom][i])
        for i in bottom, up upward.. append (matrix[i][left])
        top -= 1
        right -= 1
        bottom += 1
        left += 1

        reduce 1 every step for sprial
        at the 
        """
        ans = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #traverse left -> right
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            #traverse top right --> down right
            for i in range(top, bottom):
                ans.append(matrix[i][right -1])
            right -= 1

            if not (left < right and top < bottom):
                break
            #traverse bottom right --> bottom left
            for i in range(right-1, left - 1, -1):
                ans.append(matrix[bottom-1][i])
            bottom -= 1

            #traverse bottom left --> top left
            for i in range(bottom -1, top-1, -1):
                ans.append(matrix[i][left])
            left += 1
        
        return ans
