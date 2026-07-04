class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force, double loop
        ans = 0
        lowest = float("inf")

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                curr = prices[i] - lowest
                ans = max(curr, ans)

        return ans