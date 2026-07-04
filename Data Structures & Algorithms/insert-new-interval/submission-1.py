class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        watched vid instant

        after vid:
        given arr [intervals] each interval habve [start,end]
        given newInterval [start,end]
        insert new into arr, arr is sorted, adn non overlap, new will come in, merge if overlap, and add into this, sroted

        ok ask question? any negative, emprt, .... ok i see so can be empty, but not neg, new interval will for sure have [something,something]

        #1, O(n) go throuhg all intervals and check
        case1: overlap ? merge
        case2: new less than curr interval? add before, add rest to asn, and return right away, 
            already added new into ans, rest sorted and non overlap given
        case3: new more than curr interval, add curr into ans, keep going
        """
        ans = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # new less than curr, no overlap
                ans.append(newInterval)
                return ans + intervals[i:] #return ans + interval to end
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i]) #add curr interval, keep going next till finish condition
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        ans.append(newInterval)
        return ans #if we reach end, we merge but it didnt hit the add new Interval yet,