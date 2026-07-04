class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        string s, find longest substring without dups
        substring is like slice continuous
        return length
        ask-edge cases or other, empty substring? yes, numbers? yes, ANY ascii so syumbols and everything
        ok, 
        #1 brute, idk if there is even brute, cuz
        #2 appraoch 1, im thinking a sliding window, constraitnt is if s[rihgt] already exist, tehn we ened to shrink s[left] till we dont see s[right]
        keep a set() seen to O(1) to check if exist
        O(n) speed, since sliding window is n +n, and O(n) for space, worst case, all unique all inside seen
        not dict
        '''
        ans = left = 0
        seen = set()
        #zxyzxyz
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            seen.add(s[right])
        
        return ans