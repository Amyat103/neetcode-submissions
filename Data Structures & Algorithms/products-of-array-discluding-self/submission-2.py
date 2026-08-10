class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [nums] return nums[i] everything * except nums[i]
        Q: all ints? yes, all positive?no,
        1) have a totla sum and div?
        2) double prefix, so i cna left * right if both exist
        [1,2,8,48]
        [48,48,24,6]
        """
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        ans = [1] * len(nums)
        ans[0] = postfix[1]
        ans[-1] = prefix[-2]

        for i in range(1,len(nums)-1):
            ans[i] = prefix[i-1] * postfix[i+1]

        return ans