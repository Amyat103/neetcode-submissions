class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        given "s..", only uppercase
        given k, int
        can change up to k char in s
        return longest length substring after k replacemnet
        return longest substring where only k difference

        challenge i spot is how to tell which is most char, becuase
        if many letters and say 2As, 1b,1c,how to tell a is the most?
        
        simplest, keep a dictionary with char:count, and go through it

        A : 3
        B : 0

        dict[B] - 3
        """

        l = ans = 0
        count = defaultdict(int)
        maxf = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans
        
