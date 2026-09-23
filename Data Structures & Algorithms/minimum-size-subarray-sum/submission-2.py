class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        return min len(subarray == 10)
        questinos: sum(nums) < target? yes. empty> no min 1,no negative!!

        1) sliding window:
        - left,right start ind 0
        - if curr (sum of curr window) < target:
            right += 1
            update ans
        - if curr > target:
            curr -= left
            left += 1
        return ans when OOB
        O(n) *2n space: O(1) 
        """
        min_size = float("inf")
        left = curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                min_size = min(min_size, right-left+1)
                curr -= nums[left]
                left += 1
        
        return min_size if min_size != float("inf") else 0