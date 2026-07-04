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
        # end = len(nums)-1

        # for i in range(len(nums)-1, -1, -1):
        #     if i + nums[i] >= end:
        #         end = i
        # return end == 0
        """
        solving as DP for practice
        ask, empty? neg? no empty,a t elast 1, no neg min 0
        ok
        im thinkng a dp approach
        subproblems, trying to think starting for the front of back
        for front, starting ind 0, go through all the possible jmps, dfs(1) dfs(2).. n
        have a memory [] 
        but dont seem right
        start from back, bottom up
        dp[false] * n, start from back, last one wil auto be true, since last can reach last,
        loop backward, can i reach end with second to last yes, change secon to last to true
        now im at last -2, can i reach end? this means does dfs() retunr true, itll return False, mark it as false its fine
        now ind 1, can i reach last, itll jump for _ in range(1..n) can it reach a true, if yes, return
        yea think i found hte pattern
        DP problme with a memeory []
        where ill do a backward loop, where only last dp is true, see if dfs cna return treu each dfs 2 thign
        for i in range 1..n (jump all possible), change dp to true if one true
        at teh end return dp[0]
        time: O(n *m)? i think its not n^2 because len(nums) * average jumps each num
        space: O(n)
        """
        dp = [False] * len(nums)
        dp[-1] = True
        end = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            for jump in range(1,nums[i]+1):
                if i + jump >= end or dp[i + jump] == True:
                    dp[i] = True
                    break
        
        return dp[0]