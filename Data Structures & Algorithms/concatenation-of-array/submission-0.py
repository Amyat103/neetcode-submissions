class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        given nums, make ans array 2x the size, ans[i] = nums[i] AND 
        ans[i + n] = nums[i]
        1) init 2x size array. do a double loop, for _in 2. for i in range(nums)
        keep appending with a marker += 1
        Time: O(n), 2n -> n | space: O(n) same
        """
        n = len(nums)
        ans = [0] * (n * 2)

        pointer = add = 0

        for c in range(2):
            add = c * n
            for i in range(n):
                ans[i + add] = nums[i]
        
        return ans