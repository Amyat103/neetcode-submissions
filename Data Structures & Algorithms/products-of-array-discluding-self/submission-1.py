class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        input: [nums,...], return [product except self, ..]
        multiple everything else

        algo
        make prefix product forward and backward,
        multiple left and right since already producted
        """
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        # make prefix
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]

        # make postfix
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]
        
        ans = [0] * len(nums)

        for i in range(1, len(nums) - 1):
            ans[i] = prefix[i - 1] * postfix[i + 1]
        
        ans[0] = postfix[1]
        ans[-1] = prefix[-2]

        return ans

        
        