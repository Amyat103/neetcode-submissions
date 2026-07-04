class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [nums[0]]
        post_prod = [0] * len(nums)
        post_prod[-1] = nums[-1]
        for i in range(1, len(nums)):
            pre_prod.append(pre_prod[i - 1] * nums[i])
        # start 1 after 
        for i in range(len(nums) - 2, -1, -1):
            post_prod[i] = post_prod[i + 1] * nums[i]
        print(pre_prod)
        print(post_prod)
        ans = []

        for i in range(len(nums)):
            # checking, bound
            if i == 0:
                ans.append(post_prod[i + 1])
            elif i == len(nums) - 1:
                ans.append(pre_prod[i - 1])
            else:
                ans.append(pre_prod[i-1] * post_prod[i + 1])

        return ans




