class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        input: nums [ints...] nums[i] amount of money ith house have
        houses in straight line, rob the most, cant do adjacent hosues
        return max money can rob

        dp problme
        dp = []

        constraints, can array be empty? no
        every element will be an int, can it be neg? no

        base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]
        """
        if len(nums) <= 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]