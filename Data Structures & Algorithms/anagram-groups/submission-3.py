class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute, sort all
        # seen = defaultdict(list)

        # for word in strs:
        #     seen["".join(sorted(word))].append(word)

        # return list(seen.values())

        #above accepted but slow and prob failinterview
        # above O(nlogn), need O(n)
        seen = defaultdict(list)

        for word in strs:
            order = [0] * 26
            for letter in word:
                order[ord(letter) - ord("a")] += 1
            seen[tuple(order)].append(word)

        return list(seen.values())
