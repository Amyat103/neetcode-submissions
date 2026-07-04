class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        input: nums - [ints...] distrinct | int target
        output: [[comb],...] unique comb where they sum to target
        constraint: same num can be chosen BUT cant have dup combination: NOT: [332][323]
        return any order
        ask -- all positive? yes| empty? yes

        need to explore all ways, NOT dp cuz cant build up best way
        its find all comb

        backtracking where explore a path, come back, explore anohter
        add answer if each path works
        hard part is duplicate comb, so for this in dfs, need to track index i, where 
        1 path use indeex i, 1 path dont use, avoid dup

        algo
        dfs explore an index, nums[i],
        ex. [2,5,6,9]
        each index, 2 path, use index i, dont use index i
        avoid dup, ex. 
        curr.append(nums[i]) dfs(i, curr, total + nums[i]), # use first inex again and again
        curr.pop(), dfs(i +1, curr, total) #never use
        avoid comb
        keep an asn array outside dfs, append to it using .copy() so dont mutate array thats appendeed
        Time: (2 ^ t) because each index is 2 choices, and at most T
        space: O(
        """
        ans = []
        curr = []

        def dfs(i, curr, total):
            #found match
            if total == target:
                ans.append(curr.copy())
                return #no need to keep going, only adding more, add positive

            #didnt find match
            if total > target or i >= len(nums): # out of bound or no need to keep going since over
                return
            
            #explore 2 path
            #use current index
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            #dont use curr index
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return ans