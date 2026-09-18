class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        constriant - empty? no min 1 pile. possible (len <= h)

        1) cant add up piles nad / 9 because - dont account for x tiems per pile
        2) brute force - pikc lowest num, keep += 1 unitl first finish.
        1, curr >= 9 keep going
        2, return 2
        3) 
        use binary search, on 1-max(pile) 
        when we get mid each time:
            check if can finish, update res
            if can:
                move left side
            else:
                move right side
        """
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        
        return res