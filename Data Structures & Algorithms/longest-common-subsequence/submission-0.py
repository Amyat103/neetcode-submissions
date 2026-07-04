class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        input: text1,text2, strings
        output: int, longest common subsequence
        subsq: cat -> crabt, abcd -> abcd

        first thought, 2 pointer, but it wroks for true/false not finding best, since multile paths ect
        2nd, (IFF it go 1 dir, as in only text 1 subq of text2) maybe use letter as anchor? prob not

        Algo: make a 2d dp array n x m, len(str1 and 2)
        DP
        subproblem:
        cat
        crabt
        c==c, so rest of subproblme is 1 + (subproblem)
        at
        rabt
        a!= r, need to compare a == a, or r == t
        2 path now
        1) a == 1, so rest is t,bt
        2) rabt,t | r != t, so a,t or t (OOB)
        algo
        make 2d array, bototm up, go till the last one, return 1+ or 0+ base on match
        2 path, if match, return 1 + dp[r+1][c+1], if no match return max(dp[r+1][c+1])
        """
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)] # make 2d array with length( text1 x text2 )

        for r in range(len(text1)-1, -1, -1):
            for c in range(len(text2)-1, -1, -1):
                #case 1: if match, go diag 
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    #not same
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]