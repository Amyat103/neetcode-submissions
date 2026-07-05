class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        inputs can it be empty? no min 1| can item in preq be >< 2? exactly 2 | numCOurses at least 1? no neg?
        1) go through all prereq, map them into a dict, {courses: prereq ...}
        for loop numCourses, if 0 exist, then does 1 exist, does 2 exist. .. no
        dfs(into the dict), for loop numCourse, dfs each
        go through all path non seen, if reach every courses, return
        numCourse -1, for prereq in dict, if i dont exist return False, if ecist keep going until i reach 0 and exist, then true
        this algo is O(n*2)..
        2)
        i need to traverse the didct but its more cycle detection
        so isntead of going in and checking i need to
        dfs into 0, and keep going
        while i dfs need to track 2 var, cycle and seen, cycle is for curretnly visiting nodes, so if we see it again, theres a loop
        not possible
        seen is for after current dfs, add those into seen,
        so every dfs cases
        1) if cycle, return false
        2) if seen, last cycles , return true, that mean we traverse in a way that reach another one (still dont fully get)
        3) process by looping the rest of prereq
        """
        seen = set()
        cycle = set()
        dic = defaultdict(list)
        ans = []

        for c in prerequisites:
            dic[c[0]].append(c[1])
        
        def dfs(course):
            if course in cycle:
                return False
            elif course in seen:
                return True
            
            cycle.add(course)

            for preq in dic[course]:
                if dfs(preq) == False:
                    return False
            
            cycle.remove(course)
            seen.add(course)
            ans.append(course)
        
        for n in range(numCourses):
            if dfs(n) == False:
                return []
        return ans