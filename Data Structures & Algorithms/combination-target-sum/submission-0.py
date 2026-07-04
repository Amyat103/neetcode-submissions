class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        input: [unique nums] and int target
        return [all unique combo of nums where add to target]
        same number can be reused, unlimited of times, two combo are same if same frequent, so [2,2,3] and [3,2,2] cant both be in ans ok
        return comb in any order of num in any order ok
        ask questions -- any constraitns, empty, negative  (but shouldnt matter? neg? cuz just add and see? idk)
        and we only adding ok
        at least 1 len, num is 2-30, target 2-30 ok small problem
        ok
        #1 approach is explore all, this not dp cuz cant think of a base case, and memo building
        so for backtrack, need to explore ALL posibility, including what we just build like [2,2,2]
        so the backtrack algo will loop through all nums, for each loop, have a i,[curr],target
        start at (0,[],0), at each level, decide, over? stop the path, target? append ans and stop cuz if its over no need to keep adding all positive
        else, keep going and consider 
        speed will be ... idk actually a lot
        """
        #vars ill need
        ans = [] #global ans to append

        def search(index, curr, amount):
            #if over or found ans
            if amount > target:
                return
            if amount == target:
                ans.append(curr.copy()) #append a copy of it, pointer pointing to it
                return
            #now need to keep exploring
            for i in range(index, len(nums)):
                #start from input--each one, need to run a search
                curr.append(nums[i])
                search(i, curr, amount + nums[i])
                curr.pop()
        
        search(0,[],0)
        return ans