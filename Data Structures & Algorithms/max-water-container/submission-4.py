class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        in: [nums], act as height, return most water
        water: (right - left + 1) * min(arr[left], arr[right])
        ask: is it sorted, no| edge cases? neg? empty?? no neg at least 0, no empty, at laeast len() >= 2
        # 1 off head -- brute is there??? yea, have a max, and go through for i, for j, nested, and find max O(n^2)
        # 2, sliding window? 2 pointer? what appraich?
        not sldiing? cuz dunno when to shrink
        2 pointer? but when to move left or right, peek at if left + 1 or righjt -1 is higher? do that?
        greedy? only each step, left,right = 0, len() - 1, max=curr,max
        if left + 1 > right - 1, left+1, else right -1
        O(n) cuz we only go througn all n once, greedily
        maybe if interview say like - oh naything u think i should think, to add? differnt apprahc?
        reiterate problme + what im gonna code up agian, just to make sure
        say sth happen, interview give hint or i fail, but if hint, oh check greedy decision
        hmm ok, hint is greedy deciison,.....
        other greedy i can think of and let me analyze
        # dont move the taller wall, left right, riht taller, move left, calc, x taller move y, clac ....
        # peek forward and cac, left += 1 formula > right -= 1, move left, peek forward might past (n) more than O(1) each tiem? idk
        # if we do move the shorter wall, if same, just left += 1, prob not a big deal if same

        '''

        #first setup vars i need
        ans = 0
        left,right = 0, len(heights) - 1

        while left < right:
            curr = (right - left) * (min(heights[left], heights[right]))
            ans = max(curr, ans)
            if heights[left] > heights[right]:
                right -=1
            elif heights[left] == heights[right]:
                left += 1
            else:
                left +=1
        
        return ans