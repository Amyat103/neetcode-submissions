class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        constraints - empty? no 1. always start,end in interlva? ok
        overlap - [1,3][2,4] non-overlap - [1,2][2,3]

        1) sort()
        - [[1,2],[1,4],[2,4]]
        keep shortest end time
        Time: O(n log n) Space: O(n)
        """
        ans = 0
        intervals.sort(key = lambda x: x[1])
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            start,end = intervals[i][0], intervals[i][1]
            if start < prev:#overlap
                ans += 1
                prev = min(end, prev)
            else:
                prev = end
        
        return ans