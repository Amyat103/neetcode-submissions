class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [ints,...] - each index rep height
        return max - water i can store in array

        constraints - all ints? yes. empty arary? no least 2

        amount = width * height, NOTE: min(height1, height2)
        1) traverse elft right, remmebr a col greedely
        if curr > : move marker to curr continue: each loop calc max
        O(n) time space: O(1)
        2) two pointers, left right
        if left < right, left +=1, else: right -= 1
        area = widht * height
        O(n) time and space
        """
        max_amount = 0
        left, right = 0, len(heights) - 1

        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            max_amount = max(curr, max_amount)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_amount