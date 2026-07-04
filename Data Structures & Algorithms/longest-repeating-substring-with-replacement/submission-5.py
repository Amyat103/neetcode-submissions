class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        left = ans = larg = 0

        for right in range(len(s)):
            seen[s[right]] += 1
            larg = max(larg, seen[s[right]])
            
            while (right - left + 1) - larg > k:
                seen[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans 
            




