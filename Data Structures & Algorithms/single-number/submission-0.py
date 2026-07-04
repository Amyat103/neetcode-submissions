class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        given arr of nums, only 1 doenst gave a dup, retunr that one
        tracking dup, dict, or set, set works well since explicit twice vs one
        O(1) not work for set()
        for set i can keep adding, if in set remove, at the end only 1 itme in set, retunr set[0], because of problme constaint, it works

        saw ans: use bit mani, it works because we can keep xor, itll add minus at the end only whats left is that num
        XOR property, prob memorize, cant derive this thing too hard
        """
        ans = 0

        for n in nums:
            ans = n ^ ans
        
        return ans