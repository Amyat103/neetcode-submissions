class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        input: stirng s
        output # substring thats palidrone
        ask? empty? no min 1 letter, all leter? all letters 

        brute:
        for i in.. for j in...., double loop everything
        in the i and j range, check if palidrone, 
        O(n ^ 3), O(n^2) for loop, O(n) for checking
        algo:
        for letter in s, use it as anchor
        spread out
        count ans += 1 each time its palidrone
        O(n) for the loop
        O(n) for spreading with anchor
        2 cases
        1) odd, l, r = i +- 1
        2) even, l, r = i, i + 1
        """
        ans = 0 # start with min 1 leter, so set 1 to account for

        for i in range(len(s)):
            ans += 1
            l,r = i -1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # found palidrone
                ans += 1
                l -= 1
                r += 1
            
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans