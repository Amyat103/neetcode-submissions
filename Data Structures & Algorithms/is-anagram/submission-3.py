from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize and build seen for s
        seen = defaultdict(int)
        for letter in s:
            seen[letter] += 1

        for letter in t:
            if letter not in seen:
                return False
            seen[letter] -= 1
            if seen[letter] == 0:
                del [seen[letter]]
        
        if len(seen) != 0:
            return False
        return True