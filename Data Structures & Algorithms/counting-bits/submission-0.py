class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        given n,
        output array: [] length N +1, each index is #of 1 in a loop for i in range(n)

        bit manipulation
        algo:
        have a ans = []
        loop trhough each i in n
        for each i, loop through 32 bit, and count 1
        count = 0
        for i in range(32), if n & (1 << i): count += 1
        Why? becuase if num =3, 
        3 & (1 << 0) == 1
        3 & (1 << 1) == 1
        3 & (1 << 2) == 0
        ... all 0 rest
        count = 2, correct, 2 i's
        """
        ans = []

        for num in range(n + 1): # [0,n]
            count = 0 # for this index
            for i in range(32): # 32 bit
                if num & (1 << i): #if current bit has a 1, found by move 1 bit each time for 32 times
                    count +=  1
            ans.append(count)
        
        return ans