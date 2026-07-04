class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        maxCount = 0
        count = defaultdict(int)

        for right in range(0, len(s)):
            count[s[right]] += 1

            maxCount = max(maxCount, count[s[right]])

            while right-left + 1 - maxCount > k:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans