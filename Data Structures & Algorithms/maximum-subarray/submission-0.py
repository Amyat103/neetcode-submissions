class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        watched vid, seem sth ive seen ebfore cant reemmebr but feel like fimilar algo 
        nede to reemmebr and note

        input: [ints] array
        output: int, of largest sum

        aks- any edge cases, empty arr? 
        no? ok so len 1>len at least

        #1 brute force is to go throuhg for i,,,forj.,.. calcualte subarray, if max keep going
        but thats O(n^2) prob better
        #2 well do a for i 1 loop of n
        greedily, but not blindly though
        i feel like
        keep a curr, and ans
        if curr < 0: its neg dont even consider before its not more, only bad
        so if curr <0: then pointer at curr
        else:
            continue
        oh acutally its 2 pointer
        left, right,
        right is for right, left is track of last window
        not even 2 poiter, just keep adding no ned to re calc window
        """
        curr = 0
        ans = nums[0] #start at 0

        for right in range(len(nums)):
            if curr < 0:
                curr = nums[right]
            else:
                curr += nums[right]
            ans = max(ans, curr)
        
        return ans