class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        non decrsaing
        return 2 num, add to target
        
        list only int, non decreasieng, always have an ans
        array min len(2)? ok

        ill use left, right pointer for this, 
        return [left, right] if ans found 
        ex. numbers = [1,2,3,4], target = 3, 1 + 4 = 5, > 3, 
        right -= 1 , 4, again right -= 1, found ans retyrn [left,right]
        time: O(n) go through eveyrhign at most
        space: O(1), left, right, thats it constant
        """
        left,right = 0, len(numbers)-1

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr > target:
                right -= 1
            elif curr < target:
                left += 1
            else:
                return [left+1, right+1]
        