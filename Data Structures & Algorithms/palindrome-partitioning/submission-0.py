class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        intput: stirng s, split into all palidromic
        aab, aa b
        baab
        b aab
        ba ab
        baa b
        baab
        backtracking
        dfs(string)
        need a helper func, return bool if pali or not
        saw ans
        i knew backtrack but didnt how to use the tempalte
        so its using a index
        amnd loop 
        very brute foce, but only way
        algo:
        1) go through all indexes, use it as start, if index > len()
        went through everything and no return so its pali
        ans.append(curr)
        2) use that index or before it as anchor
        now were at new index
        for end in range(index + 1, len(nums)):
        dont get backtracking pattern thats why
        """
        ans = [] #append all ans

        def isPali(st):
            return st == st[::-1]

        def bt(i, curr):
            if i >= len(s):
                ans.append(curr.copy())
                return
            for end in range(i, len(s)):
                if isPali(s[i:end+1]):
                    curr.append(s[i:end+1])
                    bt(end+1, curr)
                    curr.pop()

        bt(0, [])
        return ans


