class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        watched vid isntanyl doing it now after vid

        given array prereq, prereq[i] is [a,b], to take b, need to take a
        [course, prereq], [want, need]
        given also numCOurse, where numCOurse is the 0-numCOurse how many courses are

        this is basically a make a graph, find cycle, if no cycle return Ture, else false
        make graph means turn our prereq and nuMCourse into a graph, using dict adn list
        and traver that dict and list, and if cycle false else true

        #1 appraoach is bsacilly 1) preprocess, defaultdict(list), for i in range(numCOurse) add each one as key,
        then go through prerqe array, course,prereq, add into dict [course]=prereq
        and now dfs(traverse all and see loop)
        dfs(each ocurse), for each course go through dict, if seen node bfore, loop, else not seen, 
        if reach end, return true, set current node as [] so no need to re cehck save a bit time
        this algo will be O(n*m) n is nodes and m is relation, or edge
        """

        # try to get all vars in 1 go
        reqMap = defaultdict(list)
        seen = set()

        #map all into a "graph"
        for course, prereq in prerequisites:
            reqMap[course].append(prereq)

        def dfs(course):
            if course in seen:
                return False
            if reqMap[course] == []: #end, can do thsi path
                return True
            seen.add(course)
            for req in reqMap[course]:
                if not dfs(req):
                    return False
            seen.remove(course)# done with this path, remove seen, so dont confuse another path
            #this course is true cuz we reach end and not false?
            reqMap[course] = []
            return True
        
        #now traverse
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

