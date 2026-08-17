class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1,s2, true - substring of s2, is permutation of s1
        constraints: empty? min 1. can s2 < s1? no ok

        1) brute: sliding window (len(s1)) move 1 by 1
        each window, sort both, if s1 == s2 after sort: true, continue
        reutnr false at end
        Time: O(n log n) sapce: O(1), store temp vars
        2) use list to count O(26) = O(1) O(n)
        same window same travelse, each window
        use array [0] * 26, compare and reutrn 
        """
        comp = [0] * 26
        for l in s1:
            comp[ord(l) - ord("a")] += 1
        
        left, right = 0, len(s1)

        for r in range(right, len(s2) + 1):
            curr = [0] * 26
            for l in s2[left : r]:
                curr[ord(l) - ord("a")] += 1
            
            if curr == comp:
                return True
            left += 1
        
        return False