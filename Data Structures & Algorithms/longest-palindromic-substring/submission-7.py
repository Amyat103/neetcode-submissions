class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        input: string s
        output: longest substring, thats palindrome
        pali - same forward backward
        ask -- empty? no min 1 | just string? yes but digit and letters

        algo, go through the s, O(n) loop, for each letter make that the anchor
        spread out O(n), spread out both ways
        case1: 1 letter as anchor, left, right = letter +- 1
        case2: 2 letters as anchor, left, right = letter1, letter2 if same
        check after each search, if right - left + 1 > ans then new ans
        time: O(n ^ 2)
        space: O(n), worst case whole thing pali
        """
        ans = s[0]

        for i in range(len(s)):
            #odd
            l, r = i - 1, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(ans):
                    ans = s[l: r+1]
                l -= 1
                r += 1
            
            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(ans):
                    ans = s[l:r + 1]
                l -= 1
                r += 1
        
        return ans
