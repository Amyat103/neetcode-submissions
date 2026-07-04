class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        loop thought the intervals starting index 1 compare to prev
        if overlap merge, append to new list, continue
        if no overlap, append prev to new list, not curr, continue
        """
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            # overlap
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])
        return ans