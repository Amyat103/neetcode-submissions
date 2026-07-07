class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        can it be empty? yes ok = []|
        make the string mapping? ok

        1) backtracking method, index? a list
        index - 2, curr = [],
        def bt(ind, curr)
            if len(curr) == len(digits): append ans.copy()
            for letter in map[ind - 2]:
                curr.append(letter)
                bt(ind +1, curr)
                curr.pop()
        bt(3,[])
        Time: n ^ n
        space: n ^n
        """
        ans = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def bt(ind, curr):
            if len(curr) == len(digits):
                ans.append(curr)
                return
            #loop through char
            for l in digitToChar[digits[ind]]:
                bt(ind + 1, curr + l)
        
        if digits:
            bt(0, "")
        return ans