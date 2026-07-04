class Solution:
    def isHappy(self, n: int) -> bool:
        """
        return if non cyclical, 
        100, == 1^2 0^2 0^2, = 1, so yes cyclical
        but how to extract 3 places
        100/10 = 10 / 10 = 1 but cant really grab 1,0,0

        after figuriegh how to grab
        keep a set(), if we are at a number we seen ebfore, inifinite loop, return False
        if == 1, return True

        oh i can just grab ok

        maybe a while loop

        looked at ans
        ned to use % and //
        % get the last digit bsaiclly, extract last digit,
        // rmeove last digit
        """
        seen = set() #if seen return False, loop
        
        def calculate(n):
            curr = 0
            while n:# while not 0
                num = n % 10 #grab last digit
                curr += (num ** 2) #doing the square
                n = n // 10 #divide by 10, floor, remove last ditig
            return curr

        while n not in seen:
            seen.add(n)
            n = calculate(n)
            if n == 1:
                return True

        return False