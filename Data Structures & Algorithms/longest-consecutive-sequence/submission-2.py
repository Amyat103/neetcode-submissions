class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        start = []
        ans = 0

        # building the initial starts
        for num in nums:
            if num - 1 not in seen:
                curr = 1
                while num+1 in seen:
                    curr+=1
                    num+=1
                ans = max(ans, curr)
                # start.append(num)

        # # building and counting conseq
        # for num in start:
        #     curr = 1
        #     while (num+1) in seen:
        #         num += 1
        #         curr += 1
        #     ans = max(ans, curr)

        return ans