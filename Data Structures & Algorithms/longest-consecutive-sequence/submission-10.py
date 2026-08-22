class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        given array of ints, return length longest. array can be any order
        constraints - empty? non intiger array? yes empty, lways int

        check candidency if i arr needs O(1) -- might need a set to check qucikly
        or dict -- but dont need to count freq, dup doenst matter, deosnt count as length

        1) set(arr) -- so i can keep checking
        1 main loop through arr: use that int keep adding?
        every iteartion do a res = max(res, curr)
        """
        res = 0
        nums_set = set(nums)

        for n in nums:
            if n - 1 in nums_set:
                continue
            else:
                curr = 0
                checkpoint = n
                while checkpoint in nums_set:
                    checkpoint += 1
                    curr += 1
                    res = max(curr, res)

        return res