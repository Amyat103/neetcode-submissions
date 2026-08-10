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

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        ans = [1] * len(nums)

        for i in range(len(nums)):
            ans[i] = prefix[i] * postfix[i]

        return ans