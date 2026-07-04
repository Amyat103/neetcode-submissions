class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        given a string s, which contain ( ) and *, retunr true/flase base on if it valid
        valid means open needs a close, and * can be wildcard ok 
        (()() -- invalid
        base on the exmaple "((**)" true since we repalce * with "" and repalce other * with )
        "(((*)" false becaue repalce ) but still not closing up

        use a stack = [] -- maintain order and i can pop and check anytime with good speed
        but need to track also a limit count too, because it shows how much erroer we can make
        doing this "(((*)" -- left = 3, star = 1, we see ), pop(), now we have left = 2, start = 1 
        if left > star:
            return false
            else true
        appraoch worng cuz dont preserver order whihc is imporant

        """
        left = []
        star = []

        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                star.append(i)
            else: #its right bracket
                #check left exist check if star exist, return false if broken order
                if not left and not star:
                    return False
                    # else one of them is there so close with it
                elif left:
                    left.pop()
                elif star:
                    star.pop()
        
        #final check saw ans, the trick is to check if any exist, if so pop, if index ( > *, out of order
        while left and star:
            if left.pop() > star.pop():
                return False #OOR
        return len(left) == 0
