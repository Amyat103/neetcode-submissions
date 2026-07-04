class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        seen = defaultdict(int)

        for right in range(len(s)):
            seen[s[right]] += 1
            while seen[s[right]] > 1 and left <= right:
                seen[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans

