class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        greedy, 
        keep track low
        if lower, change dont calc
        else, calc update max()
        cehck, can it be emty? or neg? no emty, no neg
        """
        profit = 0
        low = prices[0]

        for price in prices:
            if price < low:
                low = price
            else:
                profit = max(profit, price - low)
        return profit