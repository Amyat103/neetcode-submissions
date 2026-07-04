class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        solved dp before havent solve this i think
        input: [nums] nums[i] is money in ith mouse
        constairnt: cant rob two adjacent houses
        return max money, 1 int
        ok so adjacet house mean [1,1,3,3] cannot rob indexses, 1,2. 2,3. ect, can job indexes, 1,3.1,4 ect
        ok ask quesiton -- any constaitn, empty  array, or negative money ect
        ok no empty arrray, no neg money min is 0 ok
        #1 im thinking a dp problem, where for each step i will decide rob current house or rob next house sth like that but need to decide somehow
        idk if i can say dp(i) or dp(i + 1) mauybe its
        dp(i) or dp(i +2) that way? or no actually its dp(i) or dp(i+1) cant choose them together or its 
        nums[i] + dp(i + 2) or dp(i) sth like that>????? hmmm and then max()
        ok i think i get it genreally but need to come up with algo
        ans = 0
        memo = {} or []
        def dp(n)
        idk if start 0 or n
        if im at base case, say index 0, i can rob curernt house, or rob next one, so nums[i] + dp(i+2) or dp(i+1)
        and in those 2 dp, itll be i+2 or i+1 again 

        1. what does dp[i] mean in plain english?
        dp(i) mean robbing that house, and exploring the money well get
        2. what's the recurrence? dp[i] = f(dp[i-1], dp[i-2]...)
        recurrence is i + dp(i+2) AND i+1, those 2?
        3. what are the base cases?
        base case is if non valid index, reutrn 0, if index 1 :1, index 2:2?
        ill go bototm up, and look backward
        """
        if len(nums) == 1:
            return nums[0] #rob that only 1 house on street

        dp = [0] * (len(nums))
        #no ans cuz retunr n-1
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i - 1])
        
        return dp[-1]
