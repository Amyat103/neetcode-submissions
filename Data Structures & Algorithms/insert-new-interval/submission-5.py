class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        overlap - [1,2][2,3] non-overlap - [1,2][3,4]

        res = []
        loop each interval -> if start or end inside new interval <= >=, merge:
        if newInterval.edn < interval: add new interval, add rest arr into res return
        elif interval.end < newInterval.start: add interval to res (process rest)
        end: res.append(newInterval)

        constrtains: all intervals/newInterval 2 item only start end?. empty? yes
        time: O(n) space: O(n)
        """
        res = []

        for i in range(len(intervals)):
            #case 1: early
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            #case 2: late
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]
        
        res.append(newInterval)
        return res