class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        input int array, each element indicate how far jumo
        retyrn treu/false if can reach end from start
        1) dp solution
        keep a dp = [-1] * len(nums)
        dfs into it, dfs(i), for j in range(nums[i]), 
        if dp[j] != -1, return that cuz stored else:
        dfs(nums[j]) jump into all possible, if 0 false or sth
        2) greedy, start from the end, always check 1 before, and move
        for i in range(len -1, -1,-1), if nums[i] + i > end, if so end = i, check
        this solves the cases where [1,2,2,0,1], necause itll not move at index 3, but till move at 2, and 
        end up at 0
        """
        end = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0