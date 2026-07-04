class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        given n, whihc is 32 bit, count how many 1 bit
        ex. ..10111, 5 bits, 
        change n in place have a counter, reutnr it at the end
        """
        count = 0

        while n:
            count += 1
            n = n & (n-1)
        
        return count