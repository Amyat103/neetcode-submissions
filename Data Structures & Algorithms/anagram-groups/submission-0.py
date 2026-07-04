class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in seen:
                seen[key] = [word]
            else:
                seen[key].append(word)
        
        ans = []
        for vals in seen.values():
            ans.append(vals)
        
        return ans