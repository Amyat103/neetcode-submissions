class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        unique set of nums, return all subset
        no duplicate, any order
        does duplicate -- the order or what contains in the set()
        (2,3,2) (2,2,3) -- yes duplicate, its what contian

        1) brute force is to O(n^2) -- use index, for j in ...
        ans.apppend(i), as.append(i,j), ans.append(itoj if not in)
        
        2) brute force is actualy backtracking
        need to go through all posisble, previous dont work becuase 
        i cant just do, ans,append i, i,j, wont work for all pattern
        ill need to do a backtracking, worst time than i thought but its what i need ebcause

        algo:
        def bt(i, curr): curr []
        bt(i+1, curr[1]), that branch will chosoe put in 2 or not 2, each i 2 steps
        put in i or not put in i, this 
        """
        ans = []
        seen = set()

        def bt(index, curr):
            if tuple(curr) not in seen:
                ans.append(curr.copy())
            seen.add(tuple(curr))
            # nums = [1,2,3]. bt(0,[])|bt(1,[1])|bt(2,[1,2])|bt(3{123})
            # seocnd bt(1,[2])

            for i in range(index, len(nums)):
                curr.append(nums[i])
                bt(i+1, curr)
                curr.pop()
        
        bt(0,[])
        return ans