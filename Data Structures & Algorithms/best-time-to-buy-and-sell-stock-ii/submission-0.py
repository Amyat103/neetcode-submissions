class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2 pointers and since we see ahead, 
        buy when i + 1 is > i, while it kepe going up wait,
        tehn sell, move left pointer to riht conitneu
        """
        res = 0
        l = r = 0

        while r < len(prices) - 1:
            print(l, r)
            if prices[r + 1] >= prices[r]:
                while r < len(prices)-1 and prices[r + 1] > prices[r]:
                    r += 1
                res += (prices[r] - prices[l])
            r += 1
            l = r
        
        return res