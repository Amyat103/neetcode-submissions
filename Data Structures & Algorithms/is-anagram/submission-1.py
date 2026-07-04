from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        for i in range(len(s)):
            seen[s[i]] += 1
        
        for j in range(len(t)):
            seen[t[j]] -= 1
            if seen[t[j]] < 0:
                return False
        
        for item in seen:
            if seen[item] != 0:
                return False

        return True


        