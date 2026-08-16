class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        list of string -> group anagram together
        ana - exact letters, no more/less
        constraints - empty? yes. number as striong? no only lowercase.

        ans = []
        dict to map {}
        1) loop each word, sort the letters as key, and compare and append to dict, 
        at the end turn into a list, list(dict.keys())
        time: O(n log n) space: O(n)

        2) sort using a list -- 26 leters (52) O(1) in big o
        O(n)
        - loop each word
        in each word, make a list [0] * 26, each letter > index += 1
        (2,0,0,00...) < key
        O(n) time + space
        """
        anagram = defaultdict(list) # {key: []}

        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord("a")] += 1
            anagram[tuple(count)].append(s)
        
        return list(anagram.values())