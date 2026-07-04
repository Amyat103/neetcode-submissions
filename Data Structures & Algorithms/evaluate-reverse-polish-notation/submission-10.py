class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        given array, calculate it, its sorted in rever polish
        empty? no at least 1,
        only +-/*, ok range -200 to 200

        note: kinda in order, so earlier index go first, matter cuz / and - stuff
        CANT use 2 stack beause it losses paranthesis
        need to stick to 1 stack

        stack = []

        for each token, if its not and op, append into stack, 
        if its an op, pop 2 num out, caclualte it, push it back
        this work because
        in cases like 4,13,15 / +. suppose to be 4 + (13 / 15), if 2 stack itll be 4 / 13) + 15
        """
        stack = []

        for t in tokens:
            if t not in "+-/*":
                stack.append(t)
            else:
                num1 = int( stack.pop())
                num2 = int(stack.pop())
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "/":
                    stack.append(int(num2 / num1))
                elif t == "-":
                    stack.append(num2 - num1)
                else:
                    stack.append(num1 * num2)
        return int(stack[-1])