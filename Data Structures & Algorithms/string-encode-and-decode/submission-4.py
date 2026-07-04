class Solution:
    """
    design algo, encode: take in list output 1 str, decode take in that str, output original list
    ask -- empty? yes ok, can it be is it only letters and number? no, everything 

    cant use symbol to mark or comb to mark,
    [#][length][str] = "#lengthstr" = encode
    decode = see #, take length, str_slice: encoded[anchor:anchor+length], str_slice.append(ans)

    time: O(n), go trhough all string, add stuff, decode go thriugh that str, remove
    space: O(n - n being length of decode's s)
    """
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            add = str(len(string)) + "#" + string
            # add = "#" + length + string
            ans += add
            # "" -> "#5hello"
            # "#005hello" -> "5#hello#5david"
            #need to deal with 3 digit, right now it can be 12 lenght, and word start with 12david, mess up
            # 2 ways use first digit as legnth? so 15, 1 is lenght of lenght, 5 if legnt of str
            # or force add 0 infront 
        return ans

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            #found length s[l:r]
            length = int(s[l:r])
            l = r + 1
            r += length
            res.append(s[l:r+1])
            l = r + 1
        return res