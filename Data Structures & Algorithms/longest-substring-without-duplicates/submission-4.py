class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        in str s, find longest non repeat section (substring)
        algo is a sliding window with constraint of 1, reducing if seen or keep going

        left, right, while right not seen, keep going
        ans = max(ans, curr)
        if seen left shrink
        """
        ans = left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, (right - left + 1))
        
        return ans