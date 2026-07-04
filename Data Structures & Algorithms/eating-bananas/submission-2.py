class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles - [ints..], each i in num banana in pile
        also given h, num hours to eat all bananas
        return smallest k(banana per hour), allow koko to eat all banana
        if finish banana in under 1 hour, cant go next pile

        piles = [1,4,3,2], h = 9. 4hours, each index. 
        1) h - 4 = 5. 
        constraints. empty? no posisble? like h > len? no ok no neg? ok
        brute force -- start at len() cuz min hours
        have a var ans = max(piles)
        form there while true: check = ans -1. loop through piles, check if > 9
        loop: while h > 0. piles[i] - check,
        time: for brute: O(n*m) m is max(piles)
        2) whats a way to solve
        CHECK ANS, couldnt derive good osl
        binary serach
        using h >= len(piles) and knowing that max(piles) means k == h
        the wrost answer will always be max(piles) becuase that means
        finish each pile 1 hour, and ans == 8
        I can use max(piles) as a range and find answer, only slightly
        better than brute force, but still saves time
        range - 0 ... max(piles)
        from tehre l, r, binary search, each index/middle
        do loop(piles) check if hours <= h update ans
        """
        ans = max(piles) #worst case
        l, r = 1, max(piles)

        while l <= r:
            pace = (l + r) // 2

            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(float(pile) / pace)
                
            if curr_h > h:
                l = pace + 1
            else:
                ans = pace
                r = pace - 1
        
        return ans





