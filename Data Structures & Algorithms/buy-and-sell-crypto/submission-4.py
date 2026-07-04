class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [int,...] prices
        return max profit

        keep profit , init = 0
        each step profit = max(profit, curr)

        buy, 
        if prices[i] < buy, buy = prices[i]
        else:
            prices[i] - buy, recalc curr
        """
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                profit = max(profit, (prices[i] - buy))
        
        return profit