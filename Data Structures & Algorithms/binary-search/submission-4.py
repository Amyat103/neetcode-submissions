class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        log n time, makes it binary search, almost only possible way
        constaint, neg? ok, empty? no at least 1 len() ok same num? no all unique ok
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return -1