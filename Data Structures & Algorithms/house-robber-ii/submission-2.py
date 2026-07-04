class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        didt come up with solution, went straight to video but didnt see code in video
        because video said exactly as 1 but run twice and retunr max, so wanna be
        half practice since i watch vid for 1st soltuion 

        input: [nums] index is money in that house, unlike 1, its a circle
        constraint, get max but cant rob adjacent
        ask-- any empty arr, no at least 1, money cna be 0 but dont matter since max()

        #1 this is dp, since i saw sol, this is a run it twice and get max, this is because
        not redundant, basically its dp on same array twice but actaully getting max by indexing

        algo will go 
        dp1 [], dp2[], run dp with 2 for loop, or maybe a helper function for easier,
        tehn return max dp1,dp2
        """
        # dp1 = [0] * (len(nums))
        # dp2 = [0] * (len(nums))
        # dp1[0] = nums[0]
        # dp2[0] = nums[1]
        # dp1[1] = nums[1]
        # dp2[1] = nums[2]

        # for i in range(2, len(nums)-1):
        #     dp1[i] = max(dp1[i-2] + nums[i], dp1[i -1])
        
        # for i in range(3, len(nums)):
        #     dp2[i] = max(dp2[i-2] + nums[i], dp[i-1])
        
        # return max(dp1[-1], dp[-1])


        #helper so code cleaner?
        def dp(arr):
            dp = [0] * (len(arr))
            # base case are house 1 adn 2 houses,
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-2] + arr[i], dp[i-1]) # max of rob curr + skip 1 back, or rob last one

            return dp[-1]
        
        if len(nums) == 1:
            return nums[0] # this needed cuz constraitn is might be len 1 and algo wont work, just reutnr that 1 house
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        return max(dp(nums[:-1]), dp(nums[1:]))






