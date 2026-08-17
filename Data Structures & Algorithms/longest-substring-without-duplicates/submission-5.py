class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        return longest substring (subset of s)
        constiarnt: empty? yes. any ASCII ok

        set or dict count adn store.
        USE dict - "xxzxxy" need to keep going, and minius
        prev marker, to check and for curr ... 
        2 pointer window 
        left = 0, for right in range ...
        while break condition: left += 1 (until fixes constrint) no dupe
        each iteration res = max(res, right - left + 1)
        x:2
        y:1
        z:1
        break = string, if break <...
        """
        res = l = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1

            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res