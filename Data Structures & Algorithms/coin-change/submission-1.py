class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp problem
        where base case is dp[0] = 0
        and build up 
        from 0 to amount (inclusive), loop through all coins, if i < coin, dont calculate
        else, dp[i] = min(dp[i], dp[i - coin] + 1) 
        this is cuz dp[1]=1, 2=2,3=3,4=4, 5=1, cuz for 5 case
        5-1=4, 4 + 1, is 5
        5-5=0 + 1, = 1, which is solution
        """
        dp = [float("inf")] * (amount + 1)
        # base case 
        dp[0] = 0

        for i in range(1, amount + 1): #inclusive
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != float("inf") else -1