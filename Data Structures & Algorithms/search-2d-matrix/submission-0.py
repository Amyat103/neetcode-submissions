class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        array sorted in non decreasing BUT start of row > end of last row
        given 2d array

        check each row, left, right, half it, check sides
        how to each which row go to in

        left, right, mid
        if matrix[mid][0] > target: go left, if < target, go right, else go in
        Time: O(log n * m)
        space: O(1) no storing anything just vars
        """
        left, right = 0, len(matrix) - 1

        while left <= right:
            #outer checks, chekcing when to go into array
            mid = (right + left) // 2
            #3 cases, if target < mid[0] if target > mid[-1] or target is in there
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                #go in
                l,r = 0, len(matrix[0]) - 1
                curr = mid
                while l <= r:
                    m = (l + r) // 2
                    if target < matrix[curr][m]:
                        r = m - 1
                    elif target > matrix[curr][m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False