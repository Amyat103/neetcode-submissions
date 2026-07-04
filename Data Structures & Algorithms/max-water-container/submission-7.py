class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [int,..] are heights, return max water
        calculation = (right - left) * min(heights[right], heights[left])

        algo:
        left,right each end
        smaller moves, into other direction
        curr = clac, ans = max(curr, ans)
        O(n)
        """
        ans = 0
        left, right = 0, len(heights) - 1

        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            ans = max(ans, curr)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return ans