class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        given an array if temps, return new array where, ans[i] how many days till temp[i] get a warmer day,
        0 if no warmer day
        ask, edge caseas like empty? no least 1, ok, all ints ok, negative? no ok
        1) brute force way is double loop, for i .. for j, if found j > i temp, ans[i] = j - i + 1
        return
        2) should be faster way
        stack = []
        for i in... temps: nth in stack, append 30 in stakc
        [30,index]
        38, 38 > satck[-1]: num, ind = pop(), temp[ind] = i - ind
        with this pushing in a tuple, i can access the list again O(1) to access and mutate,
        init with all [0]s
        time: O(n) traverseing all values, O(1) op
        space: O(n) new array
        """
        ans = [0] * len(temperatures)
        stack = []
        #temperatures=[30,38,30,36,35,40,28]
        for i in range(len(temperatures)):
            #if >
            print(stack)
            while stack and temperatures[i] > stack[-1][0]:
                #if more
                _, ind = stack.pop()
                ans[ind] = i - ind
            stack.append((temperatures[i], i))
        
        return ans