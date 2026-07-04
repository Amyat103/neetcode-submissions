class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        2 outer ifs,
        1) find sorted part
            if in sorted range go in else use opposite of left/right go other

        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]: #sorted left side
                if nums[left] <= target < nums[mid]: #in left rnage
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
