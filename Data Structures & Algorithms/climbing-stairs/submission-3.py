class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = [0] * (n + 1)
        # memo[0] = 1
        # memo[1] = 1

        # for i in range(2, n+1):
        #     memo[i] = memo[i - 1] + memo[i - 2]
        
        # return memo[n]

        # top down
        # n = 2, dp(2), memo[2] = dp(1) + dp(0)
        memo = {}

        def dp(n):
            if n <= 1:
                return 1
            
            if n in memo:
                return memo[n]
            memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]
        
        return dp(n)

