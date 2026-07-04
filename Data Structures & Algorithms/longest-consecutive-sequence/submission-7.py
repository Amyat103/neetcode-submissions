class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        input [nums,...] return longest consect

        algo
        put nums in a set() first to O1 search

        lop through nums, if num - 1 not in nums, its a starting point,
        make a loop inside it, while num + 1 in nums, curr += 1, ans = max(ans ,curr)
        """
        count = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in nums:
                curr = 1
                point = num
                while point + 1 in count:
                    curr += 1
                    point += 1
                ans = max(ans, curr)
        
        return ans