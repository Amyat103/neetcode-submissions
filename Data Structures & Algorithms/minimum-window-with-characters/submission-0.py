class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case and build need from t
        if s == "" or t == "":
            return ""
        need = defaultdict(int)
        for l in t:
            need[l] += 1
        # substring dict and initialize lowest
        have = defaultdict(int)
        ans = s + "a"
        sat = set()
        left = sat_num = 0
        # ADOBECODEBANC, ABC
        for right in range(len(s)):
            have[s[right]] += 1
            if have[s[right]] >= need[s[right]] and s[right] not in sat:
                sat_num += 1
                sat.add(s[right])
            while sat_num == len(need):
                if sat_num == len(need):
                    if right-left+1 < len(ans):
                        ans = s[left:right + 1]
                have[s[left]] -= 1
                if have[s[left]] < need[s[left]]:
                    sat_num -= 1
                    sat.remove(s[left])
                left += 1
            
        if len(ans) > len(s):
            return ""
        return ans
