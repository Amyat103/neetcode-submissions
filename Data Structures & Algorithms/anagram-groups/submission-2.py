class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute, sort all
        seen = defaultdict(list)

        for word in strs:
            seen["".join(sorted(word))].append(word)

        return list(seen.values())