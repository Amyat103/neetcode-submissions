class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            while seen[s[right]] > 0:
                seen[s[left]] -= 1
                left += 1
            seen[s[right]] += 1
            ans = max(ans, right - left + 1)
        return ans