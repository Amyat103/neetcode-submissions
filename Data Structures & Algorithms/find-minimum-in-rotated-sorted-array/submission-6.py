class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        aray of unique nums -- rotate 1 to n times, n is length, at least once rotate
        return min element,
        #1 trivial O(n) brute is go through each one, keep a min var, return
        #2 but there should be eaiser, if i cant go through all and get O(n) is trivial
        rule out dict, and set ect, where will go through
        faster than On is usually logn, and only thinking binary
        not sure how to use binaryu since it uses 2 pointers, and left right, this one roated, let me try some tracing
        [3,4,5,6,1,2]
        if rotated i can see that left > right, have to be if roated unless 6 times and multiple
        so that could be 1 signal
        if i do this, lets try considering, outer is left < right, inner we check
        if num[left] > num[right] if it is, then the most is on the right side? lets test it
        let me test out thsi algo, if left > right, go right, if left < right, go left
        seem like it work in the 2 example
        is there anything im missing or not getting seem like this owudl work iwth 2 given casea nd tyring to think of other
        oh forogt to ask stuff let me ask now
        for constraint what baout empty? oh at elast 1? ok is tehr neg? oh there is negative? but shoudl work same since finding least?

        """
        #try to find all vars
        left,right = 0, len(nums) - 1
        #dont think i need min? just check? hmmm il add min for now and remove
        #ans = float("inf")

        while left <= right:#think so
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else: #==
                return nums[left]
            #no need == case, or other i think because unique nums

        #before i run, lets trace nums = [3,4,5,6,1,2]
        #1, ans 5, #2, ans 1, pass constriant left < right break, return 1
        # here left not < right, so left == right
