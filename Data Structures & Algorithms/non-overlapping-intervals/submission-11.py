class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        input: intervals - [[s, e], [s,e]]
        return min # of intervasl need to remove to amke rest non overlapping
        1,2 and 2,3 NOT overlap

        constaints? yes. empty intervals? NO

        ex [1,2][1,4][1,3][2,4][3,4]

        loop, set a intervals until the next non overlap shows up

        Time: O(n log n) sorting
        Space: O(1)
        """
        intervals.sort()
        ans = 0
        pinpoint = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= pinpoint[-1]:
                pinpoint = intervals[i]
            else:
                ans += 1
                if intervals[i][1] < pinpoint[1]:
                    pinpoint = intervals[i]
        
        return ans
