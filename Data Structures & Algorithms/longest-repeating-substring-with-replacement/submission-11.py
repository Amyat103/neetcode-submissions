class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        dict, left right pointer
        curr_most = 
        eveyrtime reach new window, dict[char] += 1, 
        curr_most = max(curr most, dict[char])
        legnth - curr_most = swaps, while swaps > k, += 1 for left
        update res at end
        """
        count = defaultdict(int)
        res = l = curr_most = 0

        for r in range(len(s)):
            count[s[r]] += 1
            curr_most = max(curr_most, count[s[r]])
            while ((r-l+1) - curr_most) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res