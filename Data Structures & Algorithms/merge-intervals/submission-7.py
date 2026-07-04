class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        input: intervals - [[starts, ends], [s, e]...]
        merge all overlapping, return any array of non overlapping intervals

        ask? empty intervals? negatives?
        - no empty, at least 1
        - no neg, 0 <= intervals
        - NOT sorted

        algorithm
        sort the intervals by start i
        loop, and append to a new array ans

        init ans = [intervals[i]]
        for i in ...: if conflict with ans[-1], ans[-1] = [max(ans[-1][intervals[i])]
        2 cases?
        no conflict: append to ans
        conflict, merge and append

        Time: O(n log n)
        Space: O(n)
        """
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if ans[-1][-1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1] = [min(ans[-1][0], intervals[i][0]), max(ans[-1][1], intervals[i][1])]
        
        return ans
