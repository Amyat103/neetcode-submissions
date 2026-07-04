class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min(left, right):
            mid = (left + right) // 2
            if left > right:
                return -1
            if nums[mid] == target:
                return mid
            # if left side is sorted
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    return find_min(left, mid - 1)
                else:
                    return find_min(mid + 1, right)
            # right is sorted and in that range
            elif nums[mid] <= nums[right]: 
                if target > nums[mid] and target <= nums[right]:
                    return find_min(mid + 1, right)
                else:
                    return find_min(left, mid - 1)
        return find_min(0, len(nums) - 1)
