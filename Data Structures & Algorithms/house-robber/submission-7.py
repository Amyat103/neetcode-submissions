class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        rob houses but no adjacent, so every step need to calculate
        should i rob this house, 
        value is ith house + i-2 (best)
        or
        i-1(best) compare which is more and chhoose that

        """
        if len(nums) == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]

