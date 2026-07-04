class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(lst, left, right):
            # this section is sorted, take left array
            if left == right or lst[right] > lst[left]:
                return lst[left]

            mid = (right + left) // 2
            if lst[mid] >= lst[left]:
                return find_min(lst, mid + 1, right)
            else:
                return find_min(lst, left, mid)
        
        return find_min(nums, 0, len(nums) - 1)
