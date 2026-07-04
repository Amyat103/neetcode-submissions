class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [2,9,8,3,6]
        one - [2,9,10,13]
        two - [9,9,12,15]
        """
        if len(nums) < 2:
            return nums[0]
        def dp(arr):
            if len(arr) < 2:
                return arr[0]
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(arr[i] + dp[i - 2], dp[i-1])
            return dp[-1]
        
        first = dp(nums[:len(nums) - 1])
        second = dp(nums[1:len(nums)])

        return max(first, second)