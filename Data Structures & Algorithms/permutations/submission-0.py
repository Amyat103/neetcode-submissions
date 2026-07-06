class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        permutation, it means all repeated combination, not subset ok
        can the len empty
        nested loop, for i
        2) backtracking
        bt(index, curr) if index == len()-1, append()
        #each step, append index + 1, use next number
        NOT index based but for n in nums, 
        O(n ^ n) 
        space(n^n)
        """
        ans = []

        def bt(curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    bt(curr)
                    curr.pop()
        
        bt([])
        return ans