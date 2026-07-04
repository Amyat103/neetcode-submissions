class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [int,...] find 3 int that == 0

        1) brute triple loop nested, for i, for j (i+1), for k (j + 1), if === 0 ans.append([...])
        O(n ^3)

        2) algo, sort, 2 loops nested
        for i in nums:
            left, right, each end,
            if > right -= 1, if < left += 1
        ned to keep a seen set() for O(1)
        O(n log n * n^2), n^2
        """
        ans = []
        seen = set()

        nums.sort()

        for i in range(len(nums) - 2):#out of bound
            left, right = i + 1, len(nums) - 1 # 2 ends
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                # if == 0 and not in seen
                if curr == 0 and (nums[i], nums[left], nums[right]) not in seen:
                    seen.add((nums[i], nums[left], nums[right]))
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1
        
        return ans