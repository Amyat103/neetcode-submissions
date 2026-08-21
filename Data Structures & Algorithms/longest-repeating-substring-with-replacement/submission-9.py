class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        longest string with at most k repalced char
        constraitns: k <= len(s). s NOT emprt, min 1

        1) dict to count char. constantly res = max(res, curr)
        problem - how to track highest count letter. var: most, (tuple). tuple[1] += 1. if letter # > tuple repalce most
        most count - (r - l + 1) = constraints
        Time: O(n) space:O(n)

        l = 0, for r in range...
        if doenst break: max = max(curr, prev)
        if break:
            while > k, left += 1, dict[l] -= 1
        """
        count = defaultdict(int)
        l = highest = 0
        ans = 0

        for r in range(len(s)):
            count[s[r]] += 1
            highest = max(highest, count[s[r]])

            while (r - l + 1) - highest > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans