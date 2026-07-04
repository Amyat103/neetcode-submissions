class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            first = numbers[left]
            second = numbers[right]
            if first + second == target:
                return [left + 1,right + 1]
            elif first + second > target:
                right -= 1
            else:
                left += 1