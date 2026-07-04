class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        ans[any nums, +/-, return 3 unique index]
        anything missing? any? oh sorted? ok
        no
        # 1, triple loop, brute force (n^3)
        for i, for j(i+1) for k(j+1) triple nested (solves it, handle unique cuz differnt points and dont overlap)
        # 2, for i in (as outer loop), 
        [-1,0,1,2,-1,-4], outer i at -1, tehn sinide i will run 2 pointer, if i -1, need next 2 to add to 1, and use the 2 pointer to +- base on what we need <0 >0 ect
        this is a O(n) other loop, O(n) inner, which means O(n^2 * n log n) BUT still n^20    for #2
        '''
        nums.sort() #[-4,-1,-1,0,1,2]
        ans = []
        seen = set() #quick check O(1), using in ans is len(ans) each cehck

        #run #1, error, time exceed, trace but dont see inf loop, just not fast engouh? ask interviewer
        # run #2, error, [0,0,0,0] fixed 
        # run #3, wrong ans missing some, cuz i had break after if () not inse en, but cuz of that break im missing some ans, switch to left += 1
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr > 0:
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    if (nums[i],nums[left],nums[right]) not in seen:
                        ans.append([nums[i],nums[left],nums[right]])
                        seen.add((nums[i],nums[left],nums[right]))
                        left += 1
                    else:
                        left += 1
        
        return ans


