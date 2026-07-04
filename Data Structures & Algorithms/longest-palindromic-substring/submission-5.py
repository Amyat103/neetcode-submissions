class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        just watched a video solutioon, right away didnt try first
        now trying

        tagged under dp but ill do two pointer way
        solution is for each letter expand out, check even odd

        input, string "s" retunr longest substring, so not num but actual stirng of longest paliondrome

        brute force is to go through every poissible, check and return like
        #1 dont really know the brute, for ecah letetr in s, check if that is aprt of paliondrome? idk

        #2 for each letter in s, to check check if its center of palidrone, so use that letter as anchor and go out
        for i, do a left,right i, i+1, go out and while going, check if its new max, set ans =""
        """
        ans = s[0] #store ans string

        for i in range(len(s)):
            # use tat lter and go out
            #odd
            left,right = i-1, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1
            
            #even
            left,right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1
        
        return ans
