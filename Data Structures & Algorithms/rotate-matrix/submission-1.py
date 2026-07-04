class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        directly watched vid

        so brute force is just space brute
        where create new 2d array, and loop and replace (idk algo really)
        
        solution is to loop from outer to inside
        using 4 pointers, each corner starting, and repalce
        top, down, left right, and replace like
        topleft, topright using indxing
        this solution replace in place, so only O(1) space, 1 "temp" var, minimum needed to replace in place

        so need left, right, and top down

        """

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                print(matrix)
                top, down = left, right

                #store top left
                topLeft = matrix[top][left + i]

                #move down left ro top left
                matrix[top][left + i] = matrix[down - i][left]

                #move down right to down left
                matrix[down - i][left] = matrix[down][right - i]

                #top right to down right
                matrix[down][right - i] = matrix[top + i][right]

                #top right get the stored top left
                matrix[top + i][right] = topLeft

            #move inside 1, will break if not valid, but need and work for even AND odd
            left += 1
            right -= 1