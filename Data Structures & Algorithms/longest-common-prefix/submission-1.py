class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        constraints - strs empty? yes ok

        1) loop go through eveyrthing

        - sort by longest -- look that direct. this could work, damage -> da, da, da..
        n log n, for sorting. 

        2) no need longest, becuase if smallest dont have need to shrink anyways

        for str in ...., expand till wrong, keep checking
        Time: O(n * m) || n - # strs, m - longest string len()
        """
        prefix = strs[0] #dance

        for s in strs:
            ind = 0

            for i in range(min(len(s), len(prefix))): #range( min(5,3)) -> range(3)
                if s[ind] != prefix[ind]: #if dance[ind] != dag[ind] break
                    break
                ind += 1 # go till da stpp
            
            prefix = s[:ind] # prefix = da
        
        return prefix