class Solution:
    def numDecodings(self, s: str) -> int:
        """
        gonna watch vid instaly
        but just thinkinging, fel like backtracking would be brute force
        maybe dp can do it with a optimized way

        since ive done dp before trying to think about even a sligh solution
        maybe for letter in s, and decode it, then check if prev + letter is valid, decode that tooo, 
        keep adding, but dont see a clear soltuon/algo and maybe if letter in seen, 
        return seen[letter] = int? so if its 12, it return 2 ways optimize
        maybe have checks, if its 1,2,0 need to try pairing
        watched solution

        kinda get it
        what i got form it is
        how many ways to decode, and not doing any decoding just how many ways
        and look at it like a decision tree, each brach is a new way kinda
        so everytime we see 1 or 2, if 1 + next ,or 2 + next is valid, then its a split,
        which means tree split, which means + 1 ways to decode

        so its a dp problme wher
        #1) loop backward
        start from the end which we will add to memo [len:1] base check
        end ; 1
        say "226"
        now we at 6, at 6 can we split deciison tree, no, 
        next 2, 2 can we split, check next, 6, 26 yues split, += 1
        next 2, can we split yes, 22, ++ 1
        return
        bsacilly that
        ask quesiton so it will be digit, ok can non empty, no really edge then
        """
        dp = {len(s) : 1}

        for i in range(len(s) - 1, -1, -1): #from last to start
            if s[i] == "0":
                dp[i] = 0
            else:
                #if not 0, then its valid
                dp[i] = dp[i + 1] # this vlaid, take form prev
                if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):#comp works cuz it conver ascii and can use string 6,7 compare
                    #next valid need to split += 1
                    dp[i] = dp[i+1] + dp[i+2]
            
        return dp[0]
