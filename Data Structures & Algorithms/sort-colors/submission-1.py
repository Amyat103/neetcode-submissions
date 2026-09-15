class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1) bubble sort
        2) three pointer, left, right, curr
        left 0s, right 2s, i will swap with left, right and eveneaullty end with 1 in middle
        i start at 0, keep inc if 1 or swap and inc
        if i == 0, swap with l, if i == 2 swpa wtih right 
        if swap left/right inc that bound because that number will be 0/2
        Time: O(n) space:O(1) just pointers
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(one, two): #swap 2 nums
            temp = nums[one]
            nums[one] = nums[two]
            nums[two] = temp

        while i <= r:
            if nums[i] == 0: #swap left
                swap(i, l)
                l += 1
            if nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
        