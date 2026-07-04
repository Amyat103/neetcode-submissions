class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute, for each num, have an ans=0, =+1, then max(ans, cur)
        # n^2
        #1) set(nums), for each num, if num + 1 in set() 1 point,
        #go through ecah points, if +1 in if +1 in. max??
        bank = set(nums)
        ans = 0

        for num in nums:
            if num -1 not in bank:
                curr = num
                while curr + 1 in bank:
                    curr  += 1
                ans = max(ans, curr - num + 1)

        return ans