class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        given int n
        output: number of 1 bit

        n is non neg ok | its 32 bit

        ex. n = 4
        brute is to loop torhough all bit
        if u & something with itself - 1, it rmeove 1 bit
        exmaple n = 21, 10111
        keep doing n & n - 1,
        firsts few opts:
        10111 &
        10110 = 10110, += 1
                10101, 
                10100, += 1
        time O(n), since if its 01111111111101,
        space O(1) tracking ans
        """
        ans = 0

        while n:
            n = n & (n - 1)
            ans += 1
        
        return ans