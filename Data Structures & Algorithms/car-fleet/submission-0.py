class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        [(7,2)(4,4)(1,1)(0,1)]
        []
        [(1.5)(1.5)(9)(10)]
        use a  stack
        first need to process the stack
        make an array []
        loop for i in range ....
        append into array with tuples, sort it, largest smallest,
        thats the stack now
        process the stack
        make a new list []
        for item in original lost, do target - [0] / [1]
        append into stack
        now process the stack
        while stack: curr = stack.pop()
        while stack[-1] <= curr, stack.pop()
        ans += 1
        time: (O n log n)
        space: O(n)
        """
        array = []
        for i in range(len(position)):
            array.append((position[i], speed[i]))
        
        #process it
        stack = []
        array.sort()
        for i in range(len(array)): #no nee dto backward ebause earliest first, and stack FILO
            stack.append((target - array[i][0]) / array[i][1])
        
        ans = 0
        while stack:
            curr = stack.pop()
            while stack and stack[-1] <= curr: #if next one is need less tiem (right behind curr car)
                stack.pop()
            ans+= 1
        
        return ans