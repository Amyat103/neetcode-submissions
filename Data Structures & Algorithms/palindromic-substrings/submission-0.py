class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        gonna wathc video instantly but i feel like i can use longest palidrome substirng and have a ans = []
        and seen = set() then using it to O(1) check already exist adn keep adding, same problme but diffenr checks

        watched video...

        watched video

        ok input string s, return # of substring, repeated ones count, so "aaa", ans have a,a,a,aa,aa,aaa, like permutation

        #1, brute is go through eac letter, inside that loop agia like a for i... for j.... and then with i and j as range,
        make a helper isPaliondrone(i,j) check, and add to ans
        but its On^3 cuz O(n^2) go through, then O(n)  to check is palidrome
        #2, optimal is 2 pointer and loop throug, so go throuhg all letter in char, and check aplidrone by going outward
        algo is
        for lette rin char, add letter into ans, then set anchor for odd, use that as middle go out and keep going while palidrone, keep adding
        for even, use letter and letter +1, keep doing smae, no need to check seen cuz aa,aa,aa valid

        """

        ans = 0

        for i in range(len(s)):
            #1, add that letter
            ans += 1

            # now use as anchor for odd
            left,right = i-1, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]: # in bound and pali
                ans += 1
                left -=1
                right += 1
            
            # now use for anchor for even
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        
        return ans