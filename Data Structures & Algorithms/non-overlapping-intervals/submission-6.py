class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        trying myself, first,

        input: [intervals] each i have start,end, 
        return min # of intervals need to remove so no overlap

        ask- is it already sorted? doent say ill assume no?
        any neg , yea neg ok i see
        each interval will be star,tend included ok, len() is at least 1 no emtpy ok

        it says min num to remove, but bsaiclly how many time need to merge,???? so its like typical 
        interval problme, if we hit conflict and merge, we ans += 1is my thinking

        #1 solution i can think of is 
        1) sort it
        2) go trhouh each one, if conflcit, merge += 1
        if not contunue
        """
        ans = 0
        intervals.sort()
        prev = intervals[0]
        print(intervals)
        

        for i in range(1, len(intervals)):# star wtih 1 so i can check back
            #check if conlfict or not
            if intervals[i][0] < prev[1]: # if conflict, merge
                #if conflict, then check the "better one" whihc means one that end earlier
                if intervals[i][1] < prev[1]:
                    prev = intervals[i]
                ans +=1
                # else no conflict, but need to switch rpev to curr
            else:
                prev = intervals[i]
                
        return ans

