class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        [prices, prices[i] price at taht day]
        1 day buy, another FUTURE to sell, return max profit, 0 if no profit, dont do neg
        ask: edge cases? empty arr, neg prices? arr will be at least 1, prices at least 0
        # 1, top of head, brute force is to nested loop, for i, for j,i+1, ans =0, max(ans) O(n^2) but works
        # 2, other solutions, 2 pointer, 0,len()-1, NO
        sliding window?, i, i+1, max=max,curr, but when to left += 1,
        greedy? always move left if right is smaller
        ex[10,1,5,6,7,1]
        start:10,1| left samller, move left, 1,5, dont move left ,calc curr and ans=max(),
        1,6, dont move left, 1,7, dont mvoe elft, ........
        this exmaple trace well, try to come up with another??
        before that this time is O(n), n+n so n, left n right n
        interview amybe add, oh seem like this is optimal, and right approch, is there anything im missing? ill code it up?
        '''
        #add all vars
        left = ans = 0 #since questions said may choose not to make txn, so 0 is best
        #left 0 since only move greediily

        for right in range(1,len(prices)):#start 1 ciz left taking that
            curr = prices[right] - prices[left]
            ans = max(ans, curr)
            if prices[right] < prices[left]:
                # did this cuz we can calcualte O1 not big deal
                # and if right is less, then, helps dups
                #=righgt cuz right is +=1 from loop so 
                left = right

        return ans