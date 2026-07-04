class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        input strs [strs,...] group anagrams togethers, return any order

        anagram exact same char combination

        grouping -- put in a list

        return [[groups],[groups]]
        
        brute force 
        1) go though each one, sort that str, put into dict

        2) go through each one, put str into a list of 26 length to count, put into tuples, and use as name for dict
        """

        # dont need ans, return list() or sth
        ans = defaultdict(list)

        for word in strs:
            curr = [0] * 26

            for letter in word:
                curr[ord(letter) - ord("a")] += 1

            ans[tuple(curr)].append(word)

        return list(ans.values())