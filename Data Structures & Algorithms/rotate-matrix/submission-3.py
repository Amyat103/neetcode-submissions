class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        rotation, rotate 90 degree, top left -> to pright, top right, bottomr ight ect keep going
        outer then move inside

        ask: any constraints, empty square? no min is [[1]] ok
        value dont matter since swapping

        algorithm im tinking is for eahc n x n, rotate n - 1 times, 
        example: 3x3, top left, top right, bottom right, bototm left, move in 1 place, and done, so 2 roattion so n - 1

        algorithm
        left, right, top bottom
        l = 0, right = n - 1, top = left, bottom = right, 
        have 1 temp variable, so topLeft = matrix[top][left], and then go backward, so only 1 temp variable
        adn move in
        time compelxity is O(n ^ 2), O(1)
        """
        left, right = 0, len(matrix[0]) - 1

        while left < right:
            for i in range(right - left): # we move in the algo, so left, right, and later left - 1 righ + 1
                top = left
                bottom = right

                topLeft = matrix[top][left + i]
                #now move backward
                # bottom left -> top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # bottom right -> bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                #top right -> bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                #top left -> top right
                matrix[top + i][right] = topLeft

            left += 1
            right -= 1

