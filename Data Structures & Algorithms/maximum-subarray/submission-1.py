class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        empty? or < 2? lenght? yes len 1, no emptyok
        2 pointers
        left, riught
        for _ in right.
        """
        res = float("-inf")
        left = curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            res = max(curr, res)
            if curr <= 0: #needs reset
                left = right + 1
                curr = 0
        
        return res