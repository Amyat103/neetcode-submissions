class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 0
        memo[1] = 1

        for i in range(2, n+1):
            if i == 2:
                memo[i] = 2
            else:
                memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]

