class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #sliding window
        ans = left = 0
        right = len(heights) - 1

        while left < right:
            curr = (right - left) * min(heights[right], heights[left])
            ans = max(ans, curr)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans