class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        input: [cost..], cost[i] need to apy and can go i+1 or i+2
        return int, lowest cost
        constrints, empty arr? at least 2? yes minlen(2). no neg cost? ok
        this sounds like a dp because of the diff start, best way, and i+1+2
        cost = [1,2,3]
        1) try dp, dp[1,2] 
        for i in range 3, dp[i] = min(cost[i] + dp[i-1], cost[i]+dp[i-2])
        dp[1,2,4], keep going 1 more? dp[-1] = min(dp[i-1],dp[i-2])
        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])

        return min(dp[-1], dp[-2])