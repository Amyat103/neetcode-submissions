class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        given non overlap intervals, [stat,end]
        input newINterval = [start,end], insert into intervals so sane order

        edge cases?, empty, yeah empty exist

        cases:
            1) newInterval is earliest, newINtervals + [intervals]
            2) newINterval in middle somehwer, for ...: if overlap, newInterval = max(curr, interval) , min (curr,intaveala)
            3) last, append(newINterval)

        time compelxity O(n)

        """
        ans = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans
            elif intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            else:
                # conflict, merge
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        ans.append(newInterval)
        return ans