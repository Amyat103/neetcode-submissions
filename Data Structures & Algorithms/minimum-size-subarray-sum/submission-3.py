class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        2 pointers, kepe a counter, if counter reach, update res, kepe going until condition

        """
        l = count = 0
        res = float("inf")

        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                res = min(res, r - l + 1)
                count -= nums[l]
                l += 1
        
        return 0 if res == float("inf") else res