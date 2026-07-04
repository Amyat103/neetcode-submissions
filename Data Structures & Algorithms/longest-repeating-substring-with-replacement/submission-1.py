class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        largest = left = ans = 0
        #{A:3, B:1}

        for right in range(len(s)):
            seen[s[right]] += 1
            largest = max(largest, seen[s[right]])

            while (right - left + 1) - largest > k:
                seen[s[left]] -= 1
                # largest = max(largest, seen[s[right]])
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans 

