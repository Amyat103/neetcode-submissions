class Solution:
    def isValid(self, s: str) -> bool:
        """
        string s only 6 unique char
        return True/False if valid
        [],{[]}, {(}
        ask - 6 unique char,empty string, only have these confirm?
        no mepty string, at least 1
        [(])
        open/close, right order
        #1 brute force -- hmm cant think of brute force nested loop cant really check valid
        #2 -- if no brute force prob dont speak out? so ill just say
        think about ordering, sth need to be close, i think about stack
        but let me think about algo
        using stack, go throuhg each char in string, if open brakcet, put into stack, if close bracket, pop stack, 
        compare, if popped one doesnt match the close braket then FALSE
        this work becuase in order for bracket to be valid can be nested but cant be out of order, so simple pop works
        for this appraoch the algo will be O(n) since ill go through the s once, each op O(1) even though mulitple 1 ops
        -- and ill say anything i might be missing or not understatind right???---ok ill code it up
        """
        #i need al the vars, for this one ill need a stack, and thats it? i think
        stack = [] # a stack if append, and pop() which pop right default, so just a array
        #oh forgot how to compare, try to think about ALL vars before continue, best i think
        #need a dict to check O(1) so no multiple ifss
        #for match i want it to be outer as key? cuz i pop outer, and check
        match = {")":"(","}": "{","]": "["}
        #"([{}])"
        # go throuhg each cahr in s
        for char in s:
            if char in match:
                #then its outer, need to pop and check
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                if top != match[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
