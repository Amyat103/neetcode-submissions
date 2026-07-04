class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'(':')', '{':'}', '[':']'}
        stack = []

        #([{
        #
        for item in s:
            if item in bracket:
                stack.append(item)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if item != bracket[check]:
                    return False
        
        return (not stack)
