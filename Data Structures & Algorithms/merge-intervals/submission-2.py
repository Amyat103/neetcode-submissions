class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        given arr of intervalsa, intervals[i] [start,end]
        merge all overlapping intervals, return array of non overlapping, that over all intervals

        question, are they sorted? this time didnt say sorted? need to srot
        constairnts? neg, or emty,

        ok no empty intervals, and no neg, ok

        so im thinking start with a 1 in for loop so i can check with prev, so i-1[0] ect to cehck 3 cases
        before, after conflcit
        before add, after add, conflcit merge ect

        #1 algo will go
        for i in range(1, len)
        if intervals[i][0]:
            its ebfore, add it to before continue
        elif prev interval's start > curr interval end, curr  # does tgus case exist, if we sorted before hand???
            no i think 2 cases?
        else: overlap, merge these 2

        2 cases
        for each i in range (1,)
        if curr interval conflict with prev, to cehck is if curr[0] < prev[1]: merge
        else, no conflict, add and skip
        time, is O(n) space also same
        """
        #think of all vars try
        # sorted(intervals, key=lambda i : i[0])
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1,len(intervals)): #starting 1
            #conflict
            if intervals[i][0] <= ans[-1][1]: #if curr start < last end, conflict
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])
        return ans